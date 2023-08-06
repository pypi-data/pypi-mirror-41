const analytics = new Vue({
    el: '#analytics',
    delimiters: ["[[", "]]"],
    data: {
        posts: {
            isLoading: false,
            results: [],
            results_backup: [],
            next: null,
            previous: null
        },
        markedPosts: [],
        filters: {
            keyword: '',
            by: '1',
            views: {
                min: 0,
                max: 500,
            },
            likes: {
                min: 0,
                max: 50,
            },
            from: null,
            to: null,
            location: ''
        },
        selectedPlatform: 'facebook',
        selectedAccount: '',
        currentAccount: {},
        accounts: {
            isLoading: false,
            results: []
        }
    },
    mixins: [SMMShared, SMMFacebook],
    watch: {
        // We have all these computed properties so we can monitor their change, because either they are nested
        // properties or we can't access their values easily from the dom, example the slider
        minViews (newValue, oldValue) {
            this.filterPosts()
        },
        maxViews (newValue, oldValue) {
            this.filterPosts()
        },
        minLikes (newValue, oldValue) {
            this.filterPosts()
        },
        maxLikes (newValue, oldValue) {
            this.filterPosts()
        },
        filter_from () {
            this.filterPosts()
        },
        filter_to () {
            this.filterPosts()
        }
    },
    filters: {
        readableDate (date) {
            return moment(date, 'X').calendar()
        }
    },
    computed: {
        allIsMarked () {
            return this.posts.results.length > 0 && this.posts.results.length === this.markedPosts.length
        },
        minViews () {
            return this.filters.views.min
        },
        maxViews () {
            return this.filters.views.max
        },
        minLikes () {
            return this.filters.likes.min
        },
        maxLikes () {
            return this.filters.likes.max
        },
        filter_from () {
            return this.filters.from
        },
        filter_to () {
            return this.filters.to
        }
    },
    methods: {
        markPost(post_id) {
            let postIndex = this.posts.results.findIndex((value, key_) => value.id === post_id)
            if (postIndex !== -1) {
                this.markedPosts.push(this.posts.results[postIndex])
            }
        },
        unMarkPost(post_id) {
            let index = this.markedPosts.findIndex((value, key_) => value.id === post_id)
            if (index !== -1) {
                this.markedPosts.splice(index, 1)
            }
        },
        markAllPosts () {
            for (let i=0; i < this.posts.results.length; i++) {
                this.markedPosts.push(this.posts.results[i])
            }
        },
        unMarkAllPosts () {
            for (let i=0; i < this.posts.results.length; i++) {
                this.markedPosts.push(this.posts.results[i])
            }
        },
        exportPosts () {
            switch (this.selectedPlatform) {
                case 'facebook':
                    this.downloadPostsCSV(this.posts.results)
                    break
                default:
                    break
            }
        },
        indexOfSelection (post_id) {
            return this.markedPosts.findIndex((value, key_) => value.id === post_id)
        },
        clearLocation () {
            this.filters.location = ''
        },
        locationChange (event) {
            const target = event.target
            const app = this
            setTimeout(function () {
                app.currentPost.location = target.value
            }, 500)
        },
        filterPosts () {
            // keyword > from to > likes > views > popularity
            this.searchPosts()
                .then(r => {
                    this.filterByDate()
                })
                .then(r => {
                    this.filterByViewsAndLikes()
                })
                .then(r => {
                    this.sortBy()
                })
        },
        filterByViewsAndLikes () {
            return new Promise(resolve => {
                const minViews = parseInt(this.filters.views.min, 10), maxViews = parseInt(this.filters.views.max, 10)
                const minLikes = parseInt(this.filters.likes.min, 10), maxLikes = parseInt(this.filters.likes.max, 10)
                this.posts.results = this.posts.results.filter(value => {
                    return minLikes <= parseInt(value.likes.summary.total_count, 10) && parseInt(value.likes.summary.total_count) <= maxLikes
                        && minViews <= parseInt(value.comments.summary.total_count, 10) && parseInt(value.comments.summary.total_count, 10) <= maxViews
                })
                resolve()
            })
        },
        fromDateChanged (event) {
            let timeString = event.target.value
            timeString = timeString.split(' ')
            const date = timeString[0].split('-')
            const time = timeString[1].split(':')
            this.filters.from = Math.round(new Date(date[0], parseInt(date[1], 10) - 1, date[2], time[0], time[1]).getTime()/1000)
        },
        toDateChanged (event) {
            let timeString = event.target.value
            timeString = timeString.split(' ')
            const date = timeString[0].split('-')
            const time = timeString[1].split(':')
            this.filters.to = Math.round(new Date(date[0], parseInt(date[1], 10) - 1, date[2], time[0], time[1]).getTime()/1000)
        },
        loadPosts() {
            this.posts.isLoading = true
            return new Promise((resolve, reject) => {
                const url = list_posts_url[this.selectedPlatform].replace('12345', this.currentAccount.id)
                HTTPClient.get(url, this.currentAccount.id)
                    .then(response => {
                        this.posts.results = response.data.data
                        this.posts.results_backup = response.data.data
                        this.posts.previous = response.data.previous
                        this.posts.next = response.data.next
                        this.posts.isLoading = false
                        resolve(response)
                    })
                    .catch(error => {
                        reject(error)
                        this.posts.isLoading = false
                        notify('Error loading posts: ' + error.response.data.error.message, 'danger', 30000)
                    })
            })
        },
        accountChange () {
            navBarInstance.isLoading = true
            this.posts.results = []
            this.posts.results_backup = []
            this.loadPosts()
                .then(resp => {
                    navBarInstance.isLoading = false
                })
                .catch(error => {
                    console.log(error.response)
                    navBarInstance.isLoading = false
                })
        },
        platformChange () {
            switch(this.selectedPlatform) {
                case 'facebook':
                    this.switchToFacebook()
                    break
                default:
                    this.accounts.isLoading = false
                    navBarInstance.isLoading = false
                    this.accounts.results = []
            }
        },
        switchToFacebook () {
            if (this.all_facebook_accounts.length === 0) {
                return new Promise((resolve, reject) => {
                    this.accounts.isLoading = true
                    this.loadAllFacebookAccounts()
                        .then(resp => {
                            this.accounts.results = this.all_facebook_accounts
                            navBarInstance.isLoading = false
                            this.accounts.isLoading = false
                            resolve(resp)
                        })
                        .catch(errors => {
                            navBarInstance.isLoading = false
                            this.accounts.isLoading = false
                            reject(errors)
                        })
                })
            }
            else {
                this.accounts.results = this.all_facebook_accounts
            }
        },
        sortBy () {
            switch(parseInt(this.filters.by, 10)) {
                case 1:
                    this.sortByDate()
                    break
                case 2:
                    this.sortByPopularity()
                    break
                case 3:
                    this.sortByLikes()
                    break
                default:
                    break
            }
        },
        filterByDate () {
            return new Promise(resolve => {
                this.posts.results = this.posts.results.filter(value => {
                    let date_created = value.created_time
                    date_created = moment(date_created, moment.ISO_8601).unix()
                    if (this.filters.from && this.filters.to) {
                        if (this.filters.from <= date_created && date_created <= this.filters.to) {
                            return value
                        }
                    }
                    else {
                        // If the from value and the to value are not set, return all the values of the list
                        return value
                    }
                })
                resolve()
            })
        },
        sortByLikes () {
            this.posts.results = this.posts.results.sort((a, b) => {
                return b.likes.summary.total_count - a.likes.summary.total_count
            })
        },
        sortByPopularity () {
            this.posts.results = this.posts.results.sort((a, b) => {
                let total_interactions_A = a.likes.summary.total_count + a.comments.summary.total_count
                let total_interactions_B = b.likes.summary.total_count + b.comments.summary.total_count
                return total_interactions_B - total_interactions_A
            })
        },
        sortByDate () {
            this.posts.results = this.posts.results.sort((a, b) => {
                let date_A = moment(a.created_date, moment.ISO_8601).unix()
                let date_B = moment(b.created_date, moment.ISO_8601).unix()
                return date_A - date_B
            })
        },
        containsTerm (searchTerm, whereToSearch) {
            if (searchTerm === '') return true
            if (!searchTerm || !whereToSearch) return false
            return whereToSearch.toLowerCase().includes(searchTerm.toLowerCase())
        },
        searchPosts () {
            return new Promise(resolve => {
                this.posts.results = this.posts.results_backup.filter(value => {
                    const searchTerm = this.filters.keyword
                    return this.containsTerm(searchTerm, value.message) ||
                        this.containsTerm(searchTerm, value.name) ||
                        this.containsTerm(searchTerm, value.link)
                })
                resolve()
            })
        },
        clearFilters () {
            this.filters = {
                keyword: '',
                by: '1',
                views: {
                    min: 0,
                    max: 500,
                },
                likes: {
                    min: 0,
                    max: 50,
                },
                from: null,
                to: null,
                location: ''
            }
        }
    },
    mounted () {
        // Load the first facebook page, if there's one
        this.switchToFacebook()
            .then(response => {
                this.currentAccount = this.facebook.pages[0]
                if (this.currentAccount.id) {
                    this.loadPosts()
                }
            })
    }
})
