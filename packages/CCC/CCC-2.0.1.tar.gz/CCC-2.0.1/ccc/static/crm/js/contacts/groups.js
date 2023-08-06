const Groups = new Vue({
    el: '#groups',
    delimiters: ["[[", "]]"],
    data: {
        groups: {
            results: [],
            next: null,
            previous: null
        },
        filters: {
            keyword: '',
        },
        group: {
            name: ''
        },
        groupAdding: false,
        groupContactsBeingViewed: null,
        groupContacts: {
            next: null,
            previous: null,
            count: null,
            results: []
        },
        page: 0
    },
    methods: {
        loadGroups (url) {
            HTTPClient.get(url)
                .then(response => {
                    this.groups = response.data
                })
                .catch(error => {
                    notify('Error occurred while loading groups', 'danger')
                })
        },
        addGroup () {
            this.groupAdding = true
            let payload = this.group
            payload['user'] = user
            HTTPClient.post('/api/contacts/groups/', payload)
                .then(resp => {
                    this.groupAdding = false
                    notify('Folder was created successfully!')
                    this.groups.results.unshift(resp.data)
                    this.group = {name: ''}
                    UIkit.modal('#add-folder-modal').hide()
                })
                .catch(error => {
                    notify('Folder failed to create!', 'danger')
                    this.groupAdding = false
                })
        },
        updateGroup () {
            this.groupAdding = true
            let payload = this.group
            payload['user'] = user
            HTTPClient.patch('/api/contacts/groups/' + this.group.id + '/', payload)
                .then(resp => {
                    this.groupAdding = false
                    notify('Folder was updated successfully!')
                    this.group = {name: ''}
                    UIkit.modal('#add-folder-modal').hide()
                })
                .catch(error => {
                    notify('Folder failed to update!', 'danger')
                    this.groupAdding = false
                })
        },
        submitGroup() {
            if (this.group.id) {
                this.updateGroup()
            }
            else {
                this.addGroup()
            }
        },
        editGroup (index) {
            this.group = this.groups.results[index]
            UIkit.modal('#add-folder-modal').show()
        },
        deleteGroup (index) {
            const group = this.groups.results[index]
            const name = `${group.name}`
            UIkit.modal.confirm("Are you sure you want to remove " + name + " from your folder list ?")
                .then(r => {
                    HTTPClient.delete('/api/contacts/groups/' + group.id + '/')
                        .then(resp => {
                            this.groups.results.splice(index, 1)
                            notify('Folder has been deleted successfully!')
                        })
                })
        },
        viewContacts (id, action=null) {
            if (!id) {
                id = this.groupContactsBeingViewed
            }
            else {
                this.groupContactsBeingViewed = id
            }

            // action can be next or previous
            let url = '/api/contacts/?group=' + id

            if (action === 'previous') {
                url = this.groupContacts.previous
            }
            else if (action === 'next') {
                url = this.groupContacts.next
            }

            HTTPClient.get(url)
                .then(response => {
                    this.groupContacts = response.data
                    UIkit.modal('#viewUsersModal').show()
                })
                .catch(error => {
                    notify(error.message, 'danger')
                })
        },
        next () {
            this.page++
            this.loadGroups(this.groups.next)
        },
        previous () {
            this.page--
            this.loadGroups(this.groups.previous)
        }
    },
    mounted () {
        this.loadGroups('/api/contacts/groups/')
    }
});
