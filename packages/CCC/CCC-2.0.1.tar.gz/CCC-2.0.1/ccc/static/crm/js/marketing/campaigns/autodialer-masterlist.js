const masterlist = new Vue({
    el: '#autodialer-masterlist',
    delimiters: ['[[', ']]'],
    data: {
        master_lists: {
            results: [],
            previous: null,
            next: null,
            count: 0
        },
        page: 0,
        dial_list_file: null
    },
    computed: {

    },
    methods: {
        dialListChanged (event) {
            this.dial_list_file = event.target.files[0]
        },
        loadMasterLists (url) {
            HTTPClient.get(url ? url : '/api/marketing/autodialer/dial/master/')
                .then(response => {
                    this.master_lists = response.data
                })
                .catch(error => {
                    notify('Error occurred loading masterlists', 'danger')
                })
        },
        next () {
            this.page++
            this.loadMasterLists(this.master_lists.next)
        },
        previous () {
            this.page--
            this.loadMasterLists(this.master_lists.previous)
        }
    },
    mounted () {
        this.loadMasterLists()
    }
});
