let navBarInstance = new Vue({
    el: '#srm-navbar',
    delimiters: ['[[', ']]'],
    data: {
        isLoading: false,
        keyword: '',
        searchResults: {
            campaigns: [],
            surveys: [],
        }
    },
    methods: {
        search () {
            if (this.keyword.length >= 3) {
                this.isLoading = true
                HTTPClient.get('/api/search/?search=' + this.keyword)
                    .then(response => {
                        Vue.set(this, 'searchResults', response.data)
                        this.isLoading = false
                    })
                    .catch(error => {
                        this.isLoading = false
                    })
            }
        },
        openContactSupport () {
            UIkit.modal('#emailSupportModal').show()
            initializeSupportEmailEditor ()
        }
    },
    computed: {
        campaigns () {
            return this.searchResults.campaigns
        },
        surveys () {
            return this.searchResults.surveys
        }
    }
})

let sortMixin = {
    methods: {
        sortBy (attribute, array=this.contacts.results) {
            if (this.sortState[attribute] === 'asc' || this.sortState[attribute] === '') {
                array = array.sort((a, b) => {
                    return a[attribute] > b[attribute]
                })
                this.sortState[attribute] = 'desc'
            }
            else {
                array = array.sort((a, b) => {
                    return b[attribute] > a[attribute]
                })
                this.sortState[attribute] = 'asc'
            }
        }
    }
}
