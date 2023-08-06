let keywords = new Vue({
    el: '#keywords',
    delimiters: ['[[', ']]'],
    data: {
        keywords: {
            results: [],
            next: null,
            previous: null,
            count: 0
        },
        surveys: {
            results: [],
            next: null,
            previous: null,
            count: 0
        },
        currentKeyword: {
            survey: '',
            keywords: ''
        },
        error: {},
        page: 0
    },
    methods: {
        loadKeywords (url_) {
            let url = url_ ? url_ : '/api/marketing/surveys/keywords/'
            HTTPClient.get(url)
                .then(response => {
                    this.keywords = response.data
                })
                .catch(error => {
                    notify('Error occurred loading keywords!')
                })
        },
        addKeyword () {
            let keywords = this.currentKeyword.keywords.trim().split(',')
            this.error = {}

            let payload = {
                survey: this.currentKeyword.survey,
                keywords: keywords.filter(word => word !== ' ')
            }

            HTTPClient.post('/api/marketing/surveys/keywords/', payload)
                .then(response => {
                    this.loadKeywords()
                    this.currentKeyword = {
                        survey: '',
                        keywords: ''
                    }
                })
                .catch(error => {
                    this.error = error.response.data
                    notify('Error occurred adding keyword!', 'danger')
                })
        },
        deleteKeyword (indexes) {
            let keyword = this.keywords.results[indexes[0]].keywords[indexes[1]]
            HTTPClient.delete('/api/marketing/surveys/keywords/' + keyword.id + '/')
                .then(response => {
                    notify('Keyword has been deleted successfully!')
                    this.keywords.results[indexes[0]].keywords.splice(indexes[1], 1)
                })
                .catch(error => {
                    notify('Error occured deleting keyword!', 'danger')
                })
        },
        loadsurveys () {
            HTTPClient.get('/api/marketing/surveys/')
                .then(response => {
                    this.surveys = response.data
                })
                .catch(error => {
                    notify('Error loading surveys', 'danger')
                })
        },
        next () {
            this.page++
            this.loadKeywords(this.keywords.next)
        },
        previous () {
            this.page--
            this.loadKeywords(this.keywords.previous)
        }
    },
    mounted () {
        this.loadKeywords()
        this.loadsurveys()
    }
})
