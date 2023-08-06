var mixin = {
    methods: {
        NextStep: function(e, response, redirect_url) {
            if (e.target.value === 'Next') {
                this.campaign_id = response.body.id;
                UIkit.modal("#addChannel").show();
            } else {
                if (redirect_url) {
                    window.location.href = redirect_url;
                }
            }
        },



        SaveData: function (e, action_url, redirect_url) {
            this.errors = [];
            var formData = new FormData(this.$el);
            if ($(this.$el).data('is_edit'))
            {
                this.$http.put(action_url, formData,
                {   headers: {
                    'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()
                    }
                }
                ).then(response => {
                        this.NextStep(e, response, redirect_url);
                }, response => {
                    if (response.status === 400 ) {
                        this.errors = response.body;
                    }
                });
            } else {
                this.$http.post(action_url, formData).then(response => {
                    this.NextStep(e, response);
                }, response => {
                    if (response.status === 400 ) {
                        this.errors = response.body;
                    } else {
                        this.NextStep(e, response, redirect_url);
                    }
                });
            }
        },
    }
}
const campaigns = new Vue({
    el: '#campaign_form',
    mixins: [mixin],
    delimiters: ["[[", "]]"],
    data: {
        campaign: {},
        campaign_id: null,
        follow_campaign_id: null,
        errors: {},
        teams: null,
        phones: null
    },
    methods: {
        CampaignForm: function (e) {
            e.preventDefault();
            const redirect_url = '/marketing/campaigns/'
            if (e.target.type === 'submit') {
                this.SaveData(e, this.$el.action, redirect_url);
            }
        },
        SaveNext: function (e) {
            this.SaveData(e, this.$el.action, null);
        }
    },
    mounted () {
        axios
        .get(this.$el.action)
        .then(response => (
            this.campaign=response.data
            )
        ),
        axios
        .get('/api/marketing/campaigns/teams/')
        .then(response => {
            if (response.data.length) {
                this.teams=response.data
            }
            }
        ),
        axios
        .get('/api/marketing/available-phone-numbers/')
        .then(response => {
            if (response.data.length) {
                this.phones=response.data
            }
            }
        )
    }
});


const sms_form = new Vue({
    el: '#SMSModal',
    mixins: [mixin],
    delimiters: ["[[", "]]"],
    data: {
        text: '',
        sample_no: '',
        send_at: '',
        ended_at: '',
        delay: '',

    }
})