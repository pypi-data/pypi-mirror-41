const redirect_numbers = new Vue({
    el: '#redirect',
    delimiters: ["[[", "]]"],
    data: {
        redirects: {
            results: [],
            next: null,
            previous: null,
            count: 0
        },
        currentRedirect: {
            campaign_number: '',
            to: ''
        },
        numbers: [],
        error: {},
        page: 0
    },
    filters: {
        DMYDate (date) {
            let date_ = new Date(date)
            return date ? date_.getDate() + '/' + (date_.getMonth() + 1) + '/' + date_.getFullYear() : ''
        }
    },
    methods: {
        loadNumbers () {
            HTTPClient.get('/api/marketing/numbers/unredirected/')
                .then(response => this.numbers = response.data)
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                })
        },
        loadRedirects (url_) {
            let url = '/api/marketing/numbers/redirects/'
            HTTPClient.get(url_ ? url_ : url)
                .then(response => this.redirects = response.data)
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                })
        },
        addRedirect () {
            let payload = {
                from_no: this.currentRedirect.campaign_number,
                to_no: this.currentRedirect.to
            }
            this.error = {}
            HTTPClient.post('/api/marketing/numbers/redirects/', payload)
                .then(response => {
                    this.redirects.results.unshift(response.data)
                    this.redirects.count += 1

                    // Remove the redirected number from list
                    let redirected_no_index = this.numbers.findIndex(num => num.twilio_number === response.data.twilio_number_object.twilio_number)
                    this.numbers.splice(redirected_no_index, 1)

                    this.currentRedirect.campaign_number = ''
                })
                .catch(error => {
                    this.error = error.response.data
                })
        },
        deleteRedirect (index) {
            let redirect = this.redirects.results[index]
            UIkit.modal.confirm('Are you sure you want to delete redirect from ' + redirect.twilio_number_object.friendly_name + ' to ' + redirect.to_no + '?')
                .then(() => {
                    HTTPClient.delete('/api/marketing/numbers/redirects/' + redirect.id)
                        .then(response => {
                            this.redirects.results.splice(index, 1)
                            notify('Redirect has been deleted!')
                            this.loadNumbers()
                            this.redirects.count -= 1
                        })
                        .catch(error => {
                            notify('Error occurred deleting redirect!', 'danger')
                        })
                })
        },
        next () {
            this.page++
            this.loadRedirects(this.redirects.next)
        },
        previous () {
            this.page--
            this.loadRedirects(this.redirects.previous)
        }
    },
    mounted () {
        this.loadNumbers()
        this.loadRedirects()
    }
})
