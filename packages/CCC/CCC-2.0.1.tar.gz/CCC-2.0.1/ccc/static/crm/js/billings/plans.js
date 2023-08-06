const CampaignNumbers = new Vue({
    el: '#campaignNumbers',
    delimiters: ["[[", "]]"],
    data: {
        check: {
            number: '',
            num_type: 'toll_free',
            country: 'US'
        },
        campaign_numbers: {
            next: null,
            previous: null,
            count: 0,
            results: [

            ]
        }
    },
    methods: {
        checkNumber () {
            UIkit.modal('#numbersModal').show()
            checkNumber.check = this.check
            checkNumber.checkNumber()
        },
        loadUsedNumbers () {
            HTTPClient.get('/api/marketing/available-phone-numbers/?fields=all')
                .then(response => this.campaign_numbers = response.data)
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                })
        }
    },
    mounted () {
        this.loadUsedNumbers()
    }
});


const checkNumber = new Vue({
    el: '#numbersModal',
    delimiters: ["[[", "]]"],
    data: {
        check: {
            number: '',
            area_code: '',
            country: 'US',
            num_type: 'toll_free'
        },
        available_numbers: [

        ],
        selected_numbers: [

        ],
        error: {

        },
        numbersLoading: false,
        buyingLoading: false,
    },
    methods: {
        checkNumber () {
            let payload = {
                num_type: this.check.num_type,
                country: this.check.country,
                area_code: this.check.area_code
            }

            if (this.check.number) {
                payload['number'] = this.check.number
            }

            this.numbersLoading = true

            HTTPClient.post('/api/marketing/check_phone_numbers/', payload)
                .then(response => {
                    this.numbersLoading = false
                    if (Array.isArray(response.data)) {
                        this.available_numbers = response.data
                    }
                    else {
                        this.available_numbers = []
                    }
                })
                .catch(error => {
                    this.numbersLoading = false
                    notify('Error occurred: ' + error.message)
                })
        },
        selectNumber (index) {
            this.selected_numbers.push(this.available_numbers[index])
            this.available_numbers.splice(index, 1)
        },
        removeNumber (index) {
            this.available_numbers.push(this.selected_numbers[index])
            this.selected_numbers.splice(index, 1)
        },
        buyNumber () {
            this.buyingLoading = true
            formData = new FormData()
            this.selected_numbers.map(number => formData.append('numbers', number.phone_number));
            HTTPClient.post('/api/marketing/buy_phone_numbers/', formData)
                .then(response => {
                    notify('Number(s) have been purchased successfully!')
                    this.selected_numbers = []
                    // Refresh numbers list
                    CampaignNumbers.loadUsedNumbers()
                    this.buyingLoading = false
                })
                .catch(error => {
                    this.buyingLoading = false
                    notify('Error occurred: ' + error.message)
                })
        },
        selectPlans () {
            this.buyingLoading = true
            formData = new FormData()
            this.selected_numbers.map(number => formData.append('numbers', number.phone_number));
            var package_ = this.$refs['package'].value
            formData.append('package', package_)
            HTTPClient.post('/packages/select-plan/', formData)
                .then(response => {
                    window.location.href = response.data.redirect_to
                })
                .catch(error => {
                    this.buyingLoading = false
                    notify('Error occurred: ' + error.message)
                })

        }
    },
    computed: {

    },
    mounted () {

    }
})
