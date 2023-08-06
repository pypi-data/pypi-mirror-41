/*
 * This script loads data for '/marketing/campaigns/<campaign_types>/<direction>'
 * Direction can be incoming or outgoing
 * So the script loads data for paths like: '/marketing/campaigns/voice/incoming/'
 * */
const loadCampaigns = {
    data () {
        return {
            campaigns: {
                next: null,
                previous: null,
                results: [],
                count: 0
            },
            errors: null,
            page: 0
        }
    },
    filters: {
        /**
         * @return {string}
         */
        DMYDate (date) {
            let date_ = new Date(date)
            return date ? (date_.getMonth() + 1) + '/' + date_.getDate() + '/' + date_.getFullYear() : ''
        }
    },
    methods: {
        loadCampaigns (url_) {
            HTTPClient.get(url_ ? url_ : url)
                .then(response => {
                    this.campaigns = response.data
                    window.scrollTo({ top: 0, behavior: 'smooth' })
                })
                .catch(error => {
                    this.errors = error.response
                    notify(error.message, 'danger')
                })
        },
        next () {
            this.page++
            this.loadCampaigns(this.campaigns.next)
        },
        previous () {
            this.page--
            this.loadCampaigns(this.campaigns.previous)
        }
    },
    mounted () {
        this.loadCampaigns()
    }
};


const filterMixin = {
    data () {
        return  {
            filter_values: {
                campaign__mappedkeywords__keyword__icontains: '',
                campaign_id: '',
                campaign__phone_id: '',
                campaign__redirect_no__to_no: '',
                // campaign__created_at__contains: '',
                date_created: ''
            },
            parent_campaigns: [],
            campaign_numbers: [],
            redirect_numbers: []
        }
    },
    methods: {
        loadParentCampaigns () {
            HTTPClient.get('/api/marketing/campaigns/')
                .then(response => {
                    this.parent_campaigns = response.data.results
                    window.scrollTo({ top: 0, behavior: 'smooth' })
                })
                .catch(error => {
                    notify('Error loading campaigns', 'danger')
                })
        },
        loadCampaignNumbers () {
            HTTPClient.get('/api/marketing/engaged-phone-numbers/?engaged_by=campaign')
                .then(response => this.campaign_numbers = response.data.results)
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                })
        },
        loadRedirectNumbers () {
            let url = '/api/marketing/numbers/redirects/'
            HTTPClient.get(url)
                .then(response => this.redirect_numbers = response.data.results)
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                })
        },
        filterCampaigns () {
            HTTPClient.get(url + '?' + dictToURLArgs(this.filter_values))
                .then(response => {
                    this.campaigns = response.data
                })
                .catch(error => {
                    this.errors = error.response
                    notify(error.message, 'danger')
                })
        },
        clearFilters () {
            this.filter_values = {
                campaign__keyword__icontains: '',
                campaign_id: '',
                campaign__phone_id: '',
                campaign__redirect_no__to_no: '',
                campaign__created_at__contains: ''
            }
            this.loadCampaigns()
        }
    },
    mounted () {
        this.loadParentCampaigns()
        this.loadRedirectNumbers()
        this.loadCampaignNumbers()
    }
}

let el = document.querySelector('#campaign-type') // This line is added because this script is shared between pages,
// so if the element does not exist, fail silently and dont print error to console
const campaign_types = el ? new Vue({
    el: '#campaign-type',
    delimiters: ["[[", "]]"],
    data: {
        conversation: '',
        sentiment_grade: '',
        sentiment_text: '',
        number_dialed: '',
        current_call_id: '',
        showSendConversationEditor: false,
        editorIsLoading: false,
        sendingConversation:false,
        error: null
    },
    mixins: [loadCampaigns, contactNotesMixin, filterMixin],
    methods: {
        showConversation (index) {
            let current_call = this.campaigns.results[index]
            this.current_call_id = current_call.id
            this.number_dialed = current_call.to
            this.error = null
            this.showSendConversationEditor = false
            if (current_call.sentiment) {
                this.sentiment_grade = current_call.sentiment.grade
                this.sentiment_text = current_call.sentiment.readable
                this.conversation = current_call.recording_text
            }
            UIkit.modal('#conversation-modal').show()
        },
        toggleConversationEditor () {
            if (!conversationEditorIsInitialized) {
                this.editorIsLoading = true
            }
            else {
                this.showSendConversationEditor = !this.showSendConversationEditor
            }
            initializeConversationEditor().then(_ => {
                CKEDITOR.instances.conversationEditor.setData(this.conversation)
                this.editorIsLoading = false
                this.showSendConversationEditor = true
            })
        },
        sendConversation (type) {
            const body = CKEDITOR.instances.conversationEditor.getData()
            let contact = this.number_dialed
            let payload = {
                type: type,
                body: body,
                contact: contact,
                call_id: this.current_call_id
            }
            this.error = null
            this.sendingConversation = true
            HTTPClient.post('/api/marketing/autodialer/' + this.current_call_id + '/send-conversation/', payload)
                .then(response => {
                    this.sendingConversation = false
                    UIkit.modal.alert('Email has been sent successfully', {stack: true})
                })
                .catch(error => {
                    this.sendingConversation = false
                    notify('Error occurred sending email', 'danger')
                    this.error = error.response.data
                })
        }
    }
}) : null




el = document.querySelector('#incoming-calls')
const incoming_calls = el ? new Vue({
    el: '#incoming-calls',
    delimiters: ["[[", "]]"],
    mixins: [loadCampaigns, filterMixin, TwilioMixin]
}) : null



el = document.querySelector('#incoming-sms')
const incoming_sms = el ? new Vue({
    el: '#incoming-sms',
    delimiters: ['[[', ']]'],
    mixins: [loadCampaigns, filterMixin],
    data: {
        sms_reply: '',
        show_input_reply_for: null
    },
    methods: {
        showReplyInput (index) {
            if (this.show_input_reply_for === index) {
                this.show_input_reply_for = null
            }
            else {
                this.show_input_reply_for = index
                setTimeout(() => {
                    this.$refs['reply-' + index.toString()][0].focus()
                }, 300)
            }
        },
        sendReply (index, isms_id) {
            HTTPClient.post(reply_sms_url, {isms_id: isms_id, reply_data: this.sms_reply})
                .then(response => {
                    this.campaigns.results[index].my_replies.push(response.data)
                    notify('Reply has been sent!')
                    this.sms_reply = ''
                })
                .catch(error => {
                    notify('Error: ' + error.response.data.error || error.message, 'danger')
                })
        }
    }
}) : null

