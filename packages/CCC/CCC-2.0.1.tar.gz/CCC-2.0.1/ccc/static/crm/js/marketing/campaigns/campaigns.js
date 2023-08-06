const campaigns = new Vue({
    el: '#campaigns',
    delimiters: ["[[", "]]"],
    data: {
        is_archive: false,
        campaigns: {
            results: [],
            previous: null,
            next: null,
            count: 0
        },
        checkedCampaigns: [],
        embedFormFor: null,
        openedFollowups: [],
        filter_data: {},
        is_card_view: window.localStorage.getItem('campaign_is_card') ? window.localStorage.getItem('campaign_is_card') : 0,
        embed_extra_fields: [],
        page: 0,
        filter: {
            name: '',
            phone: '',
            created_at: '',
            active: 'true'
        },
        engaged_numbers: {
            results: [],
        },
        sortState: {
            name: 'desc',
            created_at: '',
        },
        currentlyViewedCampaign: null
    },
    computed: {
    },
    mixins: [sortMixin],
    watch: {
        is_card_view (newVal) {
            window.localStorage.setItem('campaign_is_card', newVal)
        }
    },
    methods: {
        isOpened (key) {
            return this.openedFollowups.findIndex(value => value === key) !== -1
        },
        SearchCampaign (event) {
            var url = $(event.target).data('url');
            if (event.target.name === 'keyword') {
                url = url + '?search=' + event.target.value;
            } else {
                url = url + '?campaign_id=' + event.target.value;
            }
            if (this.is_archive)
            {
                url = url + '&archive=true'
            }
            HTTPClient.get(url).then(response => {
                this.campaigns = response.data
            });
        },
        changeCampaignView (val) {
            this.is_card_view = val
        },
        ArchivedCampaignList (event) {
            var url = $(event.target).data('url');
            var filter_url = $('#filter').data('url');
            if (!this.is_archive)
            {
                this.is_archive = true
                url = url + '?archive=true'
                filter_url = filter_url + '?archive=true'
            } else {
                this.is_archive = false
            }
            HTTPClient.get(url).then(response => {
                this.campaigns = response.data
            });
            HTTPClient.get(filter_url).then(response => {
                this.filter_data = response.data
            });
        },
        deleteCampaign(index, id, parent_campaign_id=null) {
            UIkit.modal.confirm('Are you sure about this action, this cannot be reversed!', {stack: true})
                .then(_ => {
                    const parent_index = this.campaigns.results.findIndex(val => val.id === parent_campaign_id)
                    HTTPClient.delete('/api/marketing/campaigns/' + id + '/')
                        .then(resp => {
                            console.log(index, id, parent_campaign_id, parent_index)
                            if (parent_index || parent_index === 0) {
                                this.campaigns.results[parent_index].follow_up.splice(index, 1)
                                if (this.campaigns.results[parent_index].follow_up.length === 0) {
                                    // Close the follow up dropdown
                                    this.openedFollowups.splice(index, 1)
                                }
                            }
                            else {
                                this.campaigns.results.splice(index, 1)
                            }
                            notify('Campaign was deleted successfully!')
                        })
                        .catch(error => {
                            notify('Error occurred while deleting campaign!')
                        })
                })
        },
        embedForm (event, campaign) {
            this.embedFormFor = campaign
            UIkit.modal('#embed-form-modal').show()
        },
        submitEmbedFormModal (event) {
            UIkit.modal('#embed-code-modal').show()
        },
        addNewFormField () {
            this.embed_extra_fields.push({label: ''})
        },
        removeField (index) {
            this.embed_extra_fields.splice(index, 1)
        },
        getAllEngagedPhoneNumbers () {
            HTTPClient.get('/api/marketing/engaged-phone-numbers/?engaged_by=campaign')
                .then(response => {
                    this.engaged_numbers = response.data
                })
        },
        filterCampaigns () {
            const params = dictToURLArgs(this.filter)
            HTTPClient.get('/api/marketing/campaigns/?' + params)
                .then(response => {
                    this.campaigns = response.data
                })
        },
        clearFilters () {
            this.filter = {
                name: '',
                phone: '',
                created_at: '',
                active: true
            }
            this.loadCampaigns()
        },
        loadCampaigns (url) {
            const url_ = url ? url : '/api/marketing/campaigns/'
            HTTPClient.get(url_).then(response => {
                this.campaigns = response.data
            });
        },
        viewCampaignFollowups(index) {
            this.currentlyViewedCampaign = this.campaigns.results[index]
            UIkit.modal('#followup-list').show()
        },
        next () {
            this.page++
            this.loadCampaigns(this.campaigns.next)
        },
        previous () {
            this.page--
            this.loadCampaigns(this.campaigns.previous)
        },
        sort (attribute) {
            this.sortBy(attribute, this.campaigns.results)
        }
    },
    mounted () {
        this.loadCampaigns()
        this.getAllEngagedPhoneNumbers()
        HTTPClient.get($('#filter').data('url')).then(response => {
            this.filter_data = response.data
        });
    }
});
