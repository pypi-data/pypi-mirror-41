const social_home = new Vue({
    el: '#social_home',
    delimiters: ["[[", "]]"],
    data: {
        pendingPosts: {
            next: null,
            previous: null,
            results: []
        },
        currentPost: {
            media: [],
            content: null,
            title: '',
            schedule_date: null,
            location: null,
            link: ''
        },
        selectedAccountForPost: [
        ],
        accountActionMessage: '',
        isSendingPost: false
    },
    mixins: [SMMFacebook, SMMShared],
    watch: {
    },
    computed: {

    },
    methods: {
        indexOfSelection (key) {
            return this.selectedPosts.findIndex((value, key_) => value === key)
        },
        markPost(event, key) {
            const index = this.indexOfSelection(key)
            if (index === -1) {
                this.selectedPosts.push(key)
            }
            else {
                this.selectedPosts.splice(index, 1)
            }
        },
        dateTimeChanged (event) {
            let timeString = event.target.value
            timeString = timeString.split(' ')
            const date = timeString[0].split('-')
            const time = timeString[1].split(':')
            this.currentPost.schedule_date = new Date(date[0], parseInt(date[1], 10) - 1, date[2], time[0], time[1], 0, 0)
        },
        getFormattedDateTime (dateTime) {
            if(dateTime) return moment(dateTime).format("dddd, MMMM Do YYYY, h:mm:ss a")
            return ''
        },
        postMediaChange ($event) {
            for (let i=0; i<$event.target.files.length; i++) {
                this.currentPost.media.push($event.target.files[i])
            }
        },
        removeMedia(index) {
            this.currentPost.media.splice(index, 1)
        },
        showAccountActionAlert (message, timeout=1000) {
            this.accountActionMessage = message
            setTimeout(() => {
                this.accountActionMessage = ''
            }, timeout)
        },
        selectForPost (account, platform) {
            this.accountActionMessage = ''
            account['platform'] = platform
            let canSelect = false
            //Check if it's facebook and the user has the permission to post
            if (platform.toLowerCase().includes('facebook')) {
                canSelect = this.checkIfHasFBPublishPermission(account)
            }
            if (canSelect) {
                let index = this.selectedAccountForPost.findIndex(value => value.id === account.id && value.platform === platform)
                // Add it if it has not been selected already
                if (index === -1) {
                    this.selectedAccountForPost.push(account)
                }
                else {
                    this.showAccountActionAlert('Account has been selected already!')
                }
            }
            else {
                this.showAccountActionAlert('You do not have the permission to post to this account!')
            }
        },
        submitPost () {
            this.accountActionMessage = ''

            if (this.selectedAccountForPost.length > 0) {
                navBarInstance.isLoading = true
                this.isSendingPost = true

                let target_platform_string = ''
                for (let i=0; i<this.selectedAccountForPost.length; i++) {
                    let k = i
                    target_platform_string = ''
                    const data = new FormData()
                    data.append('message', this.currentPost.content ? this.currentPost.content : '')

                    for (let i=0; i< this.currentPost.media.length; i++) {
                        data.append(`media[${i}]`, this.currentPost.media[i])
                    }

                    if (this.currentLocation.id) {
                        data.append('location', this.currentLocation.id)
                    }

                    if (this.currentPost.title) {
                        data.append('title', this.currentPost.title)
                    }

                    data.append('link', this.currentPost.link)

                    if (this.currentPost.schedule_date) {
                        data.append('schedule_date', moment(this.currentPost.schedule_date).unix())
                    }

                    // Stringify access_token + id + platform_name to form something like
                    // facebook-page|2083050545|<access_code>
                    let current = this.selectedAccountForPost[k]
                    target_platform_string += current.platform + '|' + current.id + '|' + (current.access_token ? current.access_token : '')
                    data.set('target_platform', target_platform_string)
                    // The Account object at least needs to have 'id' and 'name' attributes
                    this.sendPost(create_post_urls[current.platform],
                        data,
                        current.name,
                        this.selectedAccountForPost.length - k === 1)
                }
            }
            else {
                document.querySelector('#actionMessage').scrollIntoView({behavior: 'smooth'})
                this.accountActionMessage = 'You didn\'t select any target account!'
                setTimeout(function() {
                    document.body.scrollTop -= 40;
                }, 300)
            }
        },
        sendPost (url, data, platform_account_name, is_last) {
            console.log(url, data)
            HTTPClient.post(url, data)
                .then(response => {
                    this.isSendingPost = false

                    if (this.currentPost.schedule_date) {
                        this.reloadPendingPosts()
                    }
                    notify('Post has been published to ' + platform_account_name, 'success', 4000)
                    if (is_last) {
                        this.resetCurrentPost()
                        document.querySelector('#post-upload-form').reset()
                    }
                    resolve(response)
                })
                .catch(error => {
                    this.isSendingPost = false
                    let err = error.response.data.error ? error.response.data : null
                    if (err) {
                        err = error.response.data.error.error_user_msg || error.response.data.error.message
                    }
                    else {
                        err = error.message
                    }
                    notify('Error sending post to ' + platform_account_name + ': ' + err, 'danger', 10000)
                    reject(error)
                })
        },
        reloadPendingPosts () {
            this.pendingPosts.results = []
            this.loadAllPosts()
        },
        resetCurrentPost () {
            this.currentPost = {
                media: [],
                title: '',
                content: null,
                schedule_date: null,
                location: null,
                link: ''
            }
            this.currentLocation = {}
        },
        removeFromSelectedAccounts (index) {
            this.selectedAccountForPost.splice(index, 1)
        },
        loadAllPosts () {
            return new Promise((resolve, reject) => {
                HTTPClient.get(list_pending_post_url)
                    .then(response => {
                        this.pendingPosts = response.data
                        resolve(response)
                    })
                    .catch(error => {
                        reject(error)
                        notify('Error loading pending posts: ' + error.response.data, 'error', 30000)
                    })
            })
        },
        getAccountByTargetID (target_id) {
            let target_account = null
            // Search Pages
            this.allAccountsMixed.map(account => {
                account.id === target_id ? target_account = account : null
            })
            return target_account
        },

    },
    mounted () {
        this.loadAllFacebookAccounts()
            .then(resp => this.loadAllPosts())
    }
})
