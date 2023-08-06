/*
 * This script loads data for '/marketing/campaigns/<campaign_types>/'
 * */
const filterMixin = {
    data () {
        return  {
            filter_values: {
                campaign__mappedkeywords__keyword__icontains: '',
                campaign_id: '',
                campaign__phone_id: '',
                campaign__redirect_no__to_no: '',
                campaign__created_at__contains: ''
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
                })
                .catch(error => {
                    notify('Error loading campaigns', 'danger')
                })
        },
        loadCampaignNumbers () {
            HTTPClient.get('/api/marketing/available-phone-numbers/?fields=all')
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
                    window.scrollTo({ top: 0, behavior: 'smooth' })
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

const campaigns = new Vue({
    el: '#campaigns',
    delimiters: ["[[", "]]"],
    data: {
        campaigns: {
            next: null,
            previous: null,
            results: [],
            count: 0
        },
        errors: null,
        beingEdited: null,
        attachment: null,
        page: 0,
    },
    mixins: [filterMixin],
    filters: {
        /**
         * @return {string}
         */
        DMYDate (date) {
            let date_ = new Date(date)
            return date ? date_.getDate() + '/' + (date_.getMonth() + 1) + '/' + date_.getFullYear() : ''
        }
    },
    methods: {
        toggleEditMode (event, key) {
            this.beingEdited = this.beingEdited ? null : key
        },
        loadCampaigns (url_) {
            HTTPClient.get(url_ ? url_ : url)
                .then(response => {
                    this.campaigns = response.data
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
});
