const AutoDialerMixin = {
    data () {
        return {
            selected_campaign_number: '',
            numberToCall: '',
            campaign_numbers: [],
            autoDialingInProgress: false,
            autoDialPosition: 0,
            autoDialingPaused: false,
            callInterval: 3, // in seconds, interval between the calls
            countdown: 3,
            countdownTimer: null // Object we store the time object so we can refer to it when we need to clear
        }
    },
    watch: {
        autoDialPosition (newVal) {
            this.nextDial(newVal)
        }

    },
    computed: {
        getCountdown () {
            let mins = (parseInt(this.countdown / 60, 10)).toString()
            let seconds = (this.countdown % 60).toString()
            mins = mins.length > 1 ? mins : ('0' + mins)
            seconds = seconds.length > 1 ? seconds : ('0' + seconds)
            return mins  + ':' + seconds
        }
    },
    methods: {
        loadCampaignNumbers () {
            HTTPClient.get('/api/marketing/engaged-phone-numbers/?engaged_by=campaign')
                .then(response => this.campaign_numbers = response.data.results)
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                })
        },
        callContact (contact) {
            if (contact.phone) {
                if (this.selected_campaign_number) {
                    this.numberToCall = contact.phone
                    this.callCustomer(contact.phone, this.selected_campaign_number.twilio_number)
                }
                else {
                    UIkit.modal.alert('<p>Please select a number to use</p>')
                }
            }
            else {
                UIkit.modal.alert('<p>'+ contact.first_name  +' has no phone number attached</p>')
            }
        },
        callNumber () {
            if (this.numberToCall) {
                if (this.selected_campaign_number) {
                    this.callCustomer(this.numberToCall, this.selected_campaign_number.twilio_number)
                }
                else {
                    UIkit.modal.alert('<p>Please select a number to use</p>')
                }
            }
            else {
                UIkit.modal.alert('<p>Please enter a number to call or dial from your contacts</p>')
            }
        },
        confirmNumberSelection () {
            return new Promise((resolve, reject) => {
                if (this.selected_campaign_number) {
                    resolve()
                }
                else {
                    UIkit.modal.alert('Please select a number for this action')
                    if (this.$refs['campaign-select']) {
                        this.$refs['campaign-select'].classList.add('glow')
                        setTimeout(() => {
                            this.$refs['campaign-select'].classList.remove('glow')
                        }, 4000)
                    }
                    reject()
                }
            })
        },
        startAutoDial () {
            this.autoDialPosition = 0
            if (this.selected_campaign_number) {
                this.autoDialingInProgress = true
            }
            this.nextDial(0)
        },
        nextDial (index) {
            this.stopCountdown()
            if (index < this.contacts.results.length) {
                this.callContact(this.contacts.results[index])
                this.countdown = this.callInterval // reset the countdown
            }
            else {
                if (this.contacts.next) {
                    this.next()
                        .then(resp => {
                            this.startAutoDial()
                        })
                }
                else {
                    this.autoDialingInProgress = false
                    UIkit.modal.alert('Autodialing complete!')
                }
            }
        },
        pauseAutoDial () {
            this.autoDialingPaused = true
            this.stopCountdown()
        },
        resumeAutoDial () {
            this.autoDialingPaused = false
            this.autoDialPosition += 1
        },
        startCountdown () {
            this.countdownTimer = setInterval(this.updateCountdown, 1000)
        },
        stopCountdown () {
            clearInterval(this.countdownTimer)
            this.countdown = 0
        },
        updateCountdown () {
            if (this.countdown > 0) {
                this.countdown -= 1
            }
        }
    },
    mounted () {
        this.loadCampaignNumbers()
    }
}

const personalMessageMixin = {
    data () {
        return {
            message_search: '',
            messages: {
                results: [],
                previous: null,
                next: null,
                count: 0
            },
            isSearching: false,
            selectedMessage: null,
            played: null,
            message_to: null,
            default_voice: {},
            default_sms: {},
            active_tab: 'voice',
            personal_sms_messages: [],
            personal_voice_messages: [],
            call_sending_to: [],
            sms_sending_to: [],
            // Broadcast
            isSelectMode: false,
            isSelectAll: false,
            selectedContacts: []
        }
    },
    watch: {
    },
    methods: {
        isContactLinkDisabled (type_, contact_id) {
            if (type_ === 'voice') {
                return this.call_sending_to.includes(contact_id) ? 'disabled' : ''
            }
            else {
                return this.sms_sending_to.includes(contact_id) ? 'disabled' : ''
            }
        },
        loadMessages (url) {
            let url_ = url ? url : '/api/marketing/autodialer/personalized-messages/'
            HTTPClient.get(url_)
                .then(response => {
                    this.messages = response.data
                })
                .catch(error => {
                    notify('Error occurred loading messages', 'danger')
                })
        },
        loadVoiceMessages () {
            HTTPClient.get('/api/marketing/autodialer/personalized-messages/all/?type=voice')
                .then(response => {
                    this.personal_voice_messages = response.data
                    let default_index = response.data.findIndex(item => item.is_default)
                    this.default_voice = response.data[default_index]
                })
        },
        loadSMSMessages () {
            HTTPClient.get('/api/marketing/autodialer/personalized-messages/all/?type=sms')
                .then(response => {
                    this.personal_sms_messages = response.data
                    let default_index = response.data.findIndex(item => item.is_default)
                    this.default_sms = response.data[default_index]
                })
        },
        refreshMessages () {
            this.loadSMSMessages()
            this.loadVoiceMessages()
        },
        toggleSelectDefaultTabs (tab) {
            this.active_tab = tab
        },
        openSetDefaults () {
            UIkit.modal('#SelectMessageModal').show()
        },
        setAsDefault (type_) {
            let id = null
            if (type_ === 'voice') {
                id = this.default_voice.id
            }
            else {
                id = this.default_sms.id
            }
            HTTPClient.get('/api/marketing/autodialer/personalized-messages/' + id + '/set-as-default/')
                .then(resp => {

                })
                .catch(error => {
                    notify('Error setting as default', 'danger')
                })
        },
        searchMessage () {
            this.isSearching = true
            HTTPClient.get('/api/marketing/autodialer/personalized-messages/?page_size=1000&search=' + this.message_search + '&type=' + this.active_tab)
                .then(response => {
                    this.isSearching = false
                    if (this.active_tab === 'sms') {
                        this.personal_sms_messages = response.data.results
                    }
                    else {
                        this.personal_voice_messages = response.data.results
                    }
                })
                .catch(error => {
                    this.isSearching = false
                    notify('Error occurred searching', 'danger')
                })
        },
        playAudio (index) {
            if (this.played) {
                if (this.played.paused) {
                    this.played.play()
                }
                else {
                    this.played.pause()
                }
            }
            else {
                let url = this.personal_voice_messages[index] ? this.personal_voice_messages[index].audio : this.messages.results[index].audio
                this.played = new Audio(url)
                this.played.play()
            }
        },
        confirmDefaultSet (type_) {
            return new Promise((resolve, reject) => {
                if (type_ === 'voice') {
                    if (this.default_voice) {
                        resolve()
                    }
                    else {
                        UIkit.modal.alert('Please set a default Voice Message by clicking on <b class="srm-text-primary"><img src=' + icon + '> Configure Defaults</b> link')
                        reject()
                    }
                }
                else {
                    if (this.default_sms) {
                        resolve()
                    }
                    else {
                        UIkit.modal.alert('Please set a default SMS by clicking on <b class="srm-text-primary"><img src=' + icon + '> Configure Defaults</b> link')
                        reject()
                    }
                }
            })
        },
        sendDefaultSMS (contact_id) {
            let from = this.selected_campaign_number.twilio_number
            let payload = {
                from_: from,
                contacts: [contact_id],
            }
            this.confirmNumberSelection()
                .then(r => {
                    this.confirmDefaultSet('sms')
                        .then(r => {
                            this.sms_sending_to.push(contact_id)
                            HTTPClient.post('/api/marketing/autodialer/personalized-messages/' + this.default_sms.id + '/send/', payload)
                                .then(response => {
                                    this.sms_sending_to = []
                                    notify('SMS has been sent successfully!')
                                })
                                .catch(error => {
                                    this.sms_sending_to = []
                                    notify('Error occurred sending SMS')
                                })
                        })
                })
        },
        sendDefaultCall (contact_id) {
            let from = this.selected_campaign_number.twilio_number
            let payload = {
                from_: from,
                contacts: [contact_id],
            }
            this.confirmNumberSelection()
                .then(r => {
                    this.confirmDefaultSet('voice')
                        .then(r => {
                            this.call_sending_to.push(contact_id)
                            HTTPClient.post('/api/marketing/autodialer/personalized-messages/' + this.default_voice.id + '/send/', payload)
                                .then(response => {
                                    this.call_sending_to = []
                                    notify('Call has been sent successfully!')
                                })
                                .catch(error => {
                                    this.call_sending_to = []
                                    notify('Error occurred sending Call')
                                })
                        })
                })
        },
        closeSelectDefaults () {
            UIkit.modal('#SelectMessageModal').hide()
        },
        sendMessage () {
            let from = this.selected_campaign_number.twilio_number
            let payload = {
                from_: from,
                to: this.message_to,
            }
            HTTPClient.post('/api/marketing/autodialer/personalized-messages/' + this.selectedMessage + '/send/', payload)
                .then(response => {
                    let type_index = this.messages.results.findIndex(item => item.id === this.selectedMessage)
                    notify(this.messages.results[type_index].type + ' has been sent successfully!')
                })
                .catch(error => {
                    let type_index = this.messages.results.findIndex(item => item.id === this.selectedMessage)
                    notify('Error occurred sending ' + this.messages.results[type_index].type)
                })
        },
        sendBroadcastVoice () {
            let from = this.selected_campaign_number.twilio_number
            let payload = {
                from_: from,
                contacts: this.selectedContacts,
            }
            UIkit.dropdown('#bc-dropdown').hide()
            this.confirmNumberSelection()
                .then(r => {
                    this.confirmDefaultSet('voice')
                        .then(r => {
                            this.call_sending_to = this.selectedContacts
                            HTTPClient.post('/api/marketing/autodialer/personalized-messages/' + this.default_voice.id + '/send/', payload)
                                .then(response => {
                                    this.call_sending_to = []
                                    notify('Call has been sent successfully!')
                                })
                                .catch(error => {
                                    this.call_sending_to = []
                                    notify('Error occurred sending Call')
                                })
                        })
                })
        },
        sendBroadcastSMS () {
            let from = this.selected_campaign_number.twilio_number
            let payload = {
                from_: from,
                contacts: this.selectedContacts,
            }
            UIkit.dropdown('#bc-dropdown').hide()
            this.confirmNumberSelection()
                .then(r => {
                    this.confirmDefaultSet('sms')
                        .then(r => {
                            this.sms_sending_to = this.selectedContacts
                            HTTPClient.post('/api/marketing/autodialer/personalized-messages/' + this.default_sms.id + '/send/', payload)
                                .then(response => {
                                    this.sms_sending_to = []
                                    notify('SMS has been sent successfully!')
                                })
                                .catch(error => {
                                    this.sms_sending_to = []
                                    notify('Error occurred sending SMS')
                                })
                        })
                })
        },
        selectAllContacts () {
            if (this.isSelectAll) {
                this.isSelectAll = false
                this.selectedContacts = []
            }
            else {
                this.isSelectAll = true
                HTTPClient.get('/api/contacts/ids/?' + dictToURLArgs(this.filters))
                    .then(resp => {
                        this.selectedContacts = resp.data
                    })
            }
        },
        toggleCheckShow () {
            this.isSelectMode = !this.isSelectMode
            UIkit.dropdown('#bc-dropdown').hide()
        },
        nextPage () {
            this.loadMessages(this.messages.next)
        },
        previousPage () {
            this.loadMessages(this.messages.previous)
        }
    },
    mounted () {
        this.loadMessages()
        this.loadSMSMessages()
        this.loadVoiceMessages()
    }
}

const autoDialerContact = document.querySelector('#autodialer-contact') ?
    new Vue({
        el: '#autodialer-contact',
        delimiters: ["[[", "]]"],
        data: {
            contacts: {
                results: [],
                next: null,
                previous: null
            },
            page: 0,
            groups: [],
            campaigns: [],
            search: '',
            filters: {
                group: '',
                campaign: '',
                search: ''
            },

        },
        watch: {

        },
        computed: {

        },
        mixins: [TwilioMixin, AutoDialerMixin, personalMessageMixin, contactNotesMixin, personalizedMixin],
        methods: {
            loadContacts (url) {
                return new Promise(resolve => {
                    HTTPClient.get(url ? url : '/api/contacts/')
                        .then(response => {
                            this.contacts = response.data
                            resolve()
                            window.scrollTo({ top: 0, behavior: 'smooth' })
                        })
                        .catch(error => {
                            notify('Error occurred while loading contacts', 'danger')
                        })
                })
            },
            loadCampaigns () {
                this.campaignsLoading = true
                HTTPClient.get('/api/marketing/campaigns/?page_size=200')
                    .then(response => {
                        this.campaignsLoading = false
                        this.campaigns = response.data.results
                    })
                    .catch(error => {
                        this.campaignsLoading = false
                        notify('Couldnt load campaigns: ' + error.message)
                    })
            },
            loadGroups () {
                this.groupsLoading = true
                HTTPClient.get('/api/contacts/groups/?page_size=200')
                    .then(response => {
                        this.groupsLoading = false
                        this.groups = response.data.results
                    })
                    .catch(error => {
                        this.groupsLoading = false
                        notify('Couldn\'t load groups: ' + error.message)
                    })
            },
            searchContact () {
                HTTPClient.get('/api/contacts/?search=' + this.search)
                    .then(resp => {
                        this.contacts = resp.data
                        window.scrollTo({ top: 0, behavior: 'smooth' })
                    })
                    .catch(error => {
                        notify('Error searching contacts!')
                    })
            },
            filterContacts () {
                HTTPClient.get('/api/contacts/?' + dictToURLArgs(this.filters))
                    .then(response => {
                        this.contacts = response.data
                        window.scrollTo({ top: 0, behavior: 'smooth' })
                    })
                    .catch(error => {
                        notify('Error occurred loading contacts')
                    })
            },
            clearFilters () {
                this.filters = {
                    group: '',
                    survey: '',
                    campaign: '',
                    start_date: '',
                    end_date: '',
                }
                this.loadContacts()
            },
            next () {
                this.page++
                return new Promise(resolve => {
                    this.loadContacts(this.contacts.next)
                        .then(r => {
                            resolve()
                        })
                })
            },
            previous () {
                this.page--
                this.loadContacts(this.contacts.previous)
            }
        },
        mounted () {
            this.loadContacts()
            this.loadCampaigns()
            this.loadGroups()
        }
    }) : null

const autoDialerMasterDetail = document.querySelector('#autodialer-master-detail') ?
    new Vue({
        el: '#autodialer-master-detail',
        delimiters: ["[[", "]]"],
        mixins: [TwilioMixin, AutoDialerMixin],
        data: {
            dial_list: {
                results: [],
                count: 0,
                next: null,
                previous: null
            },
            page: 0
        },
        methods: {
            loadAutoDialList () {
                HTTPClient.get('/api/marketing/autodialer/dial/master/'+ master_list_id +'/auto-dial-list/')
                    .then(response => {
                        this.dial_list = response.data
                    })
                    .catch(error => {
                        notify('Error loading dialer list!')
                    })
            },
            callEntry (phone_number) {
                this.numberToCall = phone_number
                this.callNumber()
            }
        },
        mounted () {
            this.loadAutoDialList()
        }
    })
    : null
