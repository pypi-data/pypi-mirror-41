const reports = new Vue({
    el: '#reports',
    delimiters: ["[[", "]]"],
    mixins: [TwilioMixin],
    data: {
        toggle: 'yes',
        filter_data: {},
        account_usage: {
            "total": 0,
            "mms": 0,
            "voice": 0,
            "sms": 0,
            "email": 0
        },
        communication: {
            "sent": {
                "mms": 0,
                "voice": 0,
                "sms": 0,
                "email": 0
            },
            "receive": {
                "mms": 0,
                "voice": 0,
                "sms": 0,
                "email": 0
            },
            "account_balance": {
                "mms": 0,
                "voice": 0,
                "sms": 0,
                "email": 0
            },
            "email_analytics": [0, 0]
        },
    },
    computed: {
        datacollection: function() {
            return this.fillData()
        }
    },
    methods: {
        fillData() {
           return {
                labels: ['Sent', 'Open'],
                datasets: [
                    {
                        label: 'Email Open Rate',
                        backgroundColor: [
                           'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(54, 162, 235, 1)',
                        ],
                        borderWidth: 1,
                        data: this.communication.email_analytics
                    }
                ]
            }
        },
        SearchCampaign (event) {
            var url = $(event.target).data('url');
            url = url + '?campaign_id=' + event.target.value;
            HTTPClient.get(url).then(response => {
                this.communication = response.data;
            });
        },
        staticData (toggle) {
            var index = toggle=='yes' ? 'sent' : 'receive';
            var data = this.communication[index];
            this.account_usage = data;
            this.account_usage.total = data.voice + data.sms + data.mms + data.email;
        },
        loadCommunication () {
            url = $('#communication_static').data('analytic_url');
            HTTPClient.get(url)
                .then(response => {
                    this.communication = response.data;
                    var data = this.communication['sent'];
                    this.account_usage = data;
                    this.account_usage.total = data.voice + data.sms + data.mms + data.email;
                })
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                });
        },
        loadCampaign () {
            HTTPClient.get('/api/marketing/campaigns/').then(response => {
                this.filter_data = response.data
            });
        },
    },
    mounted () {
        this.loadCommunication();
        this.staticData('yes');
        this.loadCampaign();
    }
})

function hideDiv(x) {
    x.firstChild.classList.add("uk-hidden");
    x.getElementsByTagName('div')[1].classList.remove("uk-hidden");

}

function showDiv(x) {
    x.getElementsByTagName('div')[0].classList.remove("uk-hidden");
    x.getElementsByTagName('div')[1].classList.add("uk-hidden");
}
