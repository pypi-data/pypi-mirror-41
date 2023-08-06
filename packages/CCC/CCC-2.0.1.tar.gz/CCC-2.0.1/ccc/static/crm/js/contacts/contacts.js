const addContactMixin = {
    data () {
        return {
            campaignsLoading: false,
            groupsLoading: false,
            selected_groups: [],
            selected_campaigns: [],
        }
    },
    computed: {
        campaigns () {
            return contacts.campaigns.filter(c => !this.arrayDictIncludes(this.selected_campaigns, c))
        },
        groups () {
            return contacts.groups.filter(g => !this.arrayDictIncludes(this.selected_groups, g))
        }
    },
    methods: {
        arrayDictIncludes(array, element) {
            let exists = false
            for (let i=0; i<array.length; i++) {
                exists = array[i].id === element.id
                if (exists) {
                    break
                }
            }
            return exists
        },
        selectCampaign (index) {
            this.selected_campaigns.push(this.campaigns[index])
        },
        removeCampaign (index) {
            this.selected_campaigns.splice(index, 1)
        },
        selectGroup (index) {
            this.selected_groups.push(this.groups[index])
        },
        removeGroup (index) {
            this.selected_groups.splice(index, 1)
        },
        getAllSelectedCampaignIDs () {
            return this.selected_campaigns.map(c => c.id)
        },
        getAllSelectedFolderIDs () {
            return this.selected_groups.map(c => c.id)
        }
    }
}

const contacts = new Vue({
    el: '#contacts',
    delimiters: ["[[", "]]"],
    data: {
        contacts: {
            results: [],
            next: null,
            previous: null
        },
        page: 0,
        groups: [],
        campaigns: [],
        selectedContacts: [],
        search: '',
        filters: {
            group: '',
            survey: '',
            campaign: '',
            start_date: '',
            end_date: '',
        },
        showFilter: window.localStorage.getItem('contact_showFilters') == 'true',
        sortState: {
            first_name: 'desc',
            date_created: '',
            email: '',
            phone: '',
        }
    },
    watch: {
        showFilter (newValue, oldValue) {
            window.localStorage.setItem('contact_showFilters', newValue)
        }
    },
    computed: {

    },
    mixins: [sortMixin],
    methods: {
        loadContacts (url) {
            HTTPClient.get(url ? url : '/api/contacts/')
                .then(response => {
                    this.contacts = response.data
                    window.scrollTo({ top: 0, behavior: 'smooth' })
                })
                .catch(error => {
                    notify('Error occurred while loading contacts', 'danger')
                })
        },
        loadCampaigns () {
            this.campaignsLoading = true
            HTTPClient.get('/api/marketing/campaigns/?page_size=1000')
                .then(response => {
                    this.campaignsLoading = false
                    this.campaigns = response.data.results
                })
                .catch(error => {
                    this.campaignsLoading = false
                    notify('Couldnt load campaigns: ' + error.message)
                })
        },
        loadGroups () {
            this.groupsLoading = true
            HTTPClient.get('/api/contacts/groups/?page_size=1000')
                .then(response => {
                    this.groupsLoading = false
                    this.groups = response.data.results
                })
                .catch(error => {
                    this.groupsLoading = false
                    notify('Couldnt load groups: ' + error.message)
                })
        },
        searchContact () {
            HTTPClient.get('/api/contacts/?search=' + this.search)
                .then(resp => {
                    this.contacts = resp.data
                })
                .catch(error => {
                    notify('Error searching contacts!')
                })
        },
        filterContacts () {
            HTTPClient.get('/api/contacts/?' + dictToURLArgs(this.filters))
                .then(response => {
                    this.contacts = response.data
                    window.scrollTo({ top: 0, behavior: 'smooth' })
                })
                .catch(error => {
                    notify('Error occurred loading contacts')
                })
        },
        editContact (index) {
            const contact_to_edit = this.contacts.results[index]
            addContact.contact = contact_to_edit
            addContact.selected_campaigns = contact_to_edit.campaign_objects
            addContact.selected_groups = contact_to_edit.group_objects
            UIkit.modal('#add-contact-modal').show()
        },
        addContact () {
            addContact.resetContact()
            UIkit.modal('#add-contact-modal').show()
        },
        deleteContact (index) {
            const contact = this.contacts.results[index]
            const name = `${contact.first_name} ${contact.last_name}`
            UIkit.modal.confirm("Are you sure you want to remove " + name + " from your list ?")
                .then(r => {
                    HTTPClient.delete('/api/contacts/' + contact.id + '/')
                        .then(resp => {
                            this.contacts.results.splice(index, 1)
                            notify('Contact has been deleted successfully!')
                        })
                })
        },
        clearFilters () {
            this.filters ={
                group: '',
                survey: '',
                campaign: '',
                start_date: '',
                end_date: '',
            }
            this.loadContacts()
        },
        exportContacts () {
            window.open('/api/contacts/export_contact/', '_blank')
        },
        next () {
            this.page++
            this.loadContacts(this.contacts.next)
        },
        previous () {
            this.page--
            this.loadContacts(this.contacts.previous)
        }
    },
    mounted () {
        this.loadContacts()
        this.loadCampaigns()
        this.loadGroups()
    }
})


const addContact = new Vue({
    el: '#add-contact-modal',
    delimiters: ['[[', ']]'],
    data: {
        contact: {
            first_name: '',
            last_name: '',
            email: '',
            company_name: '',
            phone: '',
            notes: '',
            lead_type: 6, // means manual
            campaigns: []
        },
        addingContact: false,
        error: {

        }
    },
    mixins: [addContactMixin],
    computed: {
        campaigns () {
            return contacts.campaigns.filter(c => !this.arrayDictIncludes(this.selected_campaigns, c))
        },
        groups () {
            return contacts.groups.filter(g => !this.arrayDictIncludes(this.selected_groups, g))
        }
    },
    methods: {
        submitContact () {
            if (this.contact.id) {
                this.updateContact()
            }
            else {
                this.addContact()
            }
        },
        addContact () {
            this.addingContact = true
            this.error = {}
            let payload = this.contact
            payload['campaigns'] = this.getAllSelectedCampaignIDs()
            payload['groups'] = this.getAllSelectedFolderIDs()

            HTTPClient.post('/api/contacts/', payload)
                .then(response => {
                    contacts.contacts.results.unshift(response.data)
                    notify('Contact has been added!')
                    this.resetContact()
                    UIkit.modal('#add-contact-modal').hide()
                    this.addingContact = false
                })
                .catch(error => {
                    this.addingContact = false
                    this.error = error.response.data
                    this.$el.scrollTo({ top: 0, behavior: 'smooth' })
                    notify('Error occurred adding contacts!', 'danger')
                })
        },
        updateContact () {
            this.addingContact = true
            this.error = {}
            let payload = this.contact
            payload['campaigns'] = this.selected_campaigns.map(c => c.id)
            payload['groups'] = this.selected_groups.map(g => g.id)

            HTTPClient.patch('/api/contacts/' + this.contact.id + '/', payload)
                .then(response => {
                    notify('Contact has been updated!')
                    this.resetContact()
                    this.addingContact = false
                    UIkit.modal('#add-contact-modal').hide()
                })
                .catch(error => {
                    this.addingContact = false
                    this.error = error.response.data
                    this.$el.scrollTo({ top: 0, behavior: 'smooth' })
                    notify('Error occurred updating contacts!', 'danger')
                })
        },
        resetContact () {
            this.contact = {
                first_name: '',
                last_name: '',
                email: '',
                company_name: '',
                phone: '',
                notes: '',
                lead_type: 6, // means manual
                campaigns: []
            }
            this.selected_campaigns = []
            this.selected_groups = []
            this.$el.scrollTo({ top: 0, behavior: 'smooth' })
            this.error = {}
        }
    },
    mounted () {

    }
})


const import_contacts = new Vue({
    el: '#import-contact-modal',
    delimiters: ['[[', ']]'],
    mixins: [addContactMixin],
    methods: {

    }
})

const upload_contacts = new Vue({
    el: '#upload-contact-modal',
    delimiters: ['[[', ']]'],
    data: {
        contacts_file: null,
        errors: {}
    },
    mixins: [addContactMixin],
    methods: {
        contactsFileChanged (event) {
            this.contacts_file = event.target.files[0]
        },
        submitUpload () {
            let data = new FormData()
            for (let c of this.getAllSelectedCampaignIDs()) {
                data.append('campaigns', c)
            }
            for (let f of this.getAllSelectedFolderIDs()) {
                data.append('groups', f)
            }
            data.append('excel', this.contacts_file)
            data.append('drop_first_row', true)

            HTTPClient.post('/api/contacts/import_from_file/', data)
                .then(response => {
                    contacts.loadContacts()
                    UIkit.modal('#upload-contact-modal').hide()
                    notify('Success! You might need to wait for contacts imports to complete depending on size!')
                    this.selected_campaigns = []
                    this.selected_groups = []
                    this.contacts_file = null
                    document.querySelector('#contactFileFormContainer').reset() // Remove the uploaded file
                })
                .catch(error => {
                    this.errors = error.response.data
                    notify("Error: some fields are invalid! " + this.errors, 'danger')
                })
        }
    }
})

const import_system_contacts = new Vue({
    el: '#import-system-modal',
    delimiters: ['[[', ']]'],
    mixins: [addContactMixin],
    methods: {
        importUsers () {
            let data = new FormData()
            for (let c of this.getAllSelectedCampaignIDs()) {
                data.append('campaigns', c)
            }
            for (let f of this.getAllSelectedFolderIDs()) {
                data.append('groups', f)
            }

            HTTPClient.post('/api/contacts/import_system_user/', data)
                .then(response => {
                    contacts.loadContacts()
                    UIkit.modal('#import-system-modal').hide()
                    notify('Import Success!')
                })
                .catch(error => {
                    this.errors = error.response.data
                    notify("Error occurred importing contacts!" + this.errors, 'danger')
                })
        }
    }
})
