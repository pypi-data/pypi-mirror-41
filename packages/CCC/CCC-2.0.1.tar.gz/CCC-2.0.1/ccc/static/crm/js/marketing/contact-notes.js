const contactNotesMixin = {
    data () {
        return {
            currentContact: {
                first_name: ''
            },
            currentContactNotes: [],
            isCurrentlyEdited: '',
            toBeCreatedNote: {
                note: '',
                contact: ''
            },
            contactPhone: '',
            notesLoading: false
        }
    },
    methods: {
        openEditNote (index) {
            this.isCurrentlyEdited = index
            let ref = 'edit-' + index
            setTimeout(() => {
                this.$refs[ref][0].focus()
            }, 400)
        },
        saveNote () {
            let url = '/api/contacts/notes/'
            if (!this.toBeCreatedNote.contact && this.contactPhone) {
                url = '/api/contacts/notes/?contact_phone=' + this.contactPhone
            }
            HTTPClient.post(url, this.toBeCreatedNote)
                .then(resp => {
                    this.currentContactNotes.unshift(resp.data)
                    this.toBeCreatedNote.note = ''
                })
                .catch(error => {
                    notify('Error saving notes')
                })
        },
        deleteNote (index, id) {
            HTTPClient.delete('/api/contacts/notes/' + id + '/')
                .then(resp => {
                    this.currentContactNotes.splice(index, 1)
                })
                .catch(error => {
                    notify('Error occurred while deleting note')
                })
        },
        editNote (index) {
            HTTPClient.patch('/api/contacts/notes/' + this.currentContactNotes[index].id + '/',
                this.currentContactNotes[index])
                .then(resp => {
                    notify('Note has been updated')
                    this.isCurrentlyEdited = ''
                })
                .catch(error => {
                    notify('Error occurred modifying note')
                })
        },
        loadNotesForContactByPhoneNumber (phone) {
            this.currentContactNotes = []
            UIkit.modal('#contactNotesModal').show()
            this.notesLoading = true
            if (phone) {
                this.contactPhone = phone
                this.currentContact.first_name = phone
                // This value is used for other pages where contact lists are not available like call log
            }
            HTTPClient.get('/api/contacts/notes/?contact_phone=' + phone)
                .then(resp => {
                    this.notesLoading = false
                    this.currentContactNotes = resp.data
                })
                .catch(error => {
                    this.notesLoading = false
                    notify('An error occurred while loading contact notes')
                })
        },
        loadNotesForContacts (index) {
            this.currentContactNotes = []
            UIkit.modal('#contactNotesModal').show()
            this.currentContact = this.contacts.results[index]
            this.toBeCreatedNote.contact = this.currentContact.id
            this.notesLoading = true
            HTTPClient.get('/api/contacts/notes/?contact_id=' + this.currentContact.id)
                .then(resp => {
                    this.notesLoading = false
                    this.currentContactNotes = resp.data
                })
                .catch(error => {
                    this.notesLoading = false
                    notify('An error occurred while loading notes for ' + this.currentContact.first_name)
                })
        },
        closeNotes () {
            UIkit.modal('#contactNotesModal').hide()
            this.currentContactNotes = []
            this.currentContact = ''
        }
    }
}
