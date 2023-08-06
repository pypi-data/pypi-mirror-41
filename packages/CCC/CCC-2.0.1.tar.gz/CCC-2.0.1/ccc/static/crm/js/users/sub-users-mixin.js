const subUsersMixin = {
    data () {
        return {
            subUser: {
                first_name: '',
                last_name: '',
                email: ''
            },
            subUsers: [],
            viewedParentList: [],
            subUsersLoading: false,
            loading: false,
            errors: null
        }
    },
    computed: {
        currentViewedParent () {
            return this.viewedParentList.length > 0 ? this.viewedParentList[this.viewedParentList.length - 1] : null
        },
        currentViewParentName () {
            if (this.currentViewedParent) {
                return this.currentViewedParent.name
            }
            return first_name
        }
    },
    methods: {
        addSubUser () {
            this.loading = true
            this.errors = null
            let url = '/api/users/sub/'
            if (this.currentViewedParent) {
                url = '/api/users/sub/?parent=' + this.currentViewedParent.id
            }
            HTTPClient.post(url, this.subUser)
                .then(response => {
                    UIkit.modal.alert('Invitation has been sent successfully to ' + this.subUser.first_name)
                    this.loading = false
                    this.subUser = {
                        first_name: '',
                        last_name: '',
                        email: ''
                    }
                    this.viewSubUsers()
                })
                .catch(error => {
                    this.errors = error.response.data
                    this.loading = false
                })
        },
        viewSubUsers () {
            this.viewedParentList = []
            this.subUsersLoading = true
            HTTPClient.get('/api/users/sub/')
                .then(response => {
                    if (document.querySelector('#viewUsersModal')) {
                        UIkit.modal('#viewUsersModal').show()
                    }
                    this.subUsers = response.data
                    this.subUsersLoading = false
                })
                .catch(error => {
                    this.subUsersLoading = false
                    notify('Error loading sub-users', 'danger')
                })
        },
        onSubUserView (user_id, user_name) {
            this.subUsersLoading = true
            HTTPClient.get('/api/users/sub/?parent=' + user_id)
                .then(response => {
                    this.subUsers = response.data
                    this.viewedParentList.push({id: user_id, name: user_name})
                    this.subUsersLoading = false
                })
                .catch(error => {
                    this.subUsersLoading = false
                    notify('Error loading sub-users', 'danger')
                })
        },
        disableUserAccount (user_id, index) {
            HTTPClient.patch('/api/users/' + user_id + '/', {is_active: false})
                .then(resp => {
                    this.subUsers[index].is_active = false
                })
                .catch(error => {
                    notify('Error occurred disabling user account')
                })
        },
        enableUserAccount (user_id, index) {
            HTTPClient.patch('/api/users/' + user_id + '/', {is_active: true})
                .then(resp => {
                    this.subUsers[index].is_active = true
                })
                .catch(error => {
                    notify('Error occurred disabling user account')
                })
        },
        backTheUserTree () {
            this.viewedParentList.pop()
            if (this.currentViewedParent) {
                this.onSubUserView(this.currentViewedParent.id, this.currentViewedParent.name)
            }
            else {
                this.viewSubUsers()
            }
        }
    },
    mounted () {
        this.viewSubUsers()
    }
}
