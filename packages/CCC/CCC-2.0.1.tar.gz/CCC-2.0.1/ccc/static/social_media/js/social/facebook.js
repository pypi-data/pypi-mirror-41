const SMMFacebook = {
    data: {
        facebook: {
            users: [],
            groups: [],
            pages: [],
        },
        all_facebook_accounts: []
    },
    methods: {
        getConnectedFacebookAccounts () {
            navBarInstance.isLoading = true
            return new Promise((resolve, reject) => {
                HTTPClient.get(connected_accounts_url)
                    .then(response => {
                        this.updateFacebookUsers(response.data)
                        this.updateAllAccountsList(response.data)
                        this.updateAllFacebookAccountsList(response.data)
                        resolve(response)
                    })
                    .catch(error => {
                        reject(error)
                        this.errors.push({platform: 'facebook',
                            message: error.response.data.error.message,
                            readable: 'Facebook Users Error'})
                    })
            })
        },
        updateAllAccountsList (account_list) {
            for (let i=0; i < account_list.length; i++) {
                this.allAccountsMixed.push(account_list[i])
            }
        },
        updateAllFacebookAccountsList (account_list) {
            for (let i=0; i < account_list.length; i++) {
                this.all_facebook_accounts.push(account_list[i])
            }
        },
        getAccountPages (facebook_user_id=null) {
            const url = facebook_user_id !== null ? account_pages_url + '?facebook_user_id=' + facebook_user_id : account_pages_url
            return new Promise((resolve, reject) => {
                HTTPClient.get(url)
                    .then(response => {
                        resolve(response)
                        this.updateFacebookPages(response.data.data)
                        this.updateAllAccountsList(response.data.data)
                        this.updateAllFacebookAccountsList(response.data.data)
                    })
                    .catch(error => {
                        reject(error)
                        this.errors.push({platform: 'facebook',
                            message: error.response.data.error.message,
                            readable: 'Facebook Pages Error'})
                    })
            })
        },
        getAccountGroups (facebook_user_id=null) {
            const url = facebook_user_id !== null ? account_groups_url + '?facebook_user_id=' + facebook_user_id : account_groups_url
            return new Promise((resolve, reject) => {
                HTTPClient.get(account_groups_url)
                    .then(response => {
                        this.updateFacebookGroups(response.data.data)
                        this.updateAllAccountsList(response.data.data)
                        this.updateAllFacebookAccountsList(response.data.data)
                        resolve(response)
                    })
                    .catch(error => {
                        this.errors.push({platform: 'facebook',
                            message: error.response.data.error.message,
                            readable: 'Facebook Groups Error'})
                        reject(error)
                    })
            })
        },
        checkIfHasFBPublishPermission (account) {
              if (account.platform && account.platform === 'facebook-group') {
                  const has = account.permissions.findIndex(item => item.toLowerCase().includes('publish'))
                  return has !== -1
              }
              return true
        },
        facebookAuth () {
            navBarInstance.isLoading = true
            window.location.href = facebook_auth_url
        },
        facebookLogout (facebook_uid) {
            navBarInstance.isLoading = true
            let logout_url = facebook_uid === 'all' ? facebook_logout_url : facebook_logout_url + '?facebook_uid=' + facebook_uid
            window.location.href = logout_url
        },
        updateFacebookPages (new_pages) {
            for (let i=0; i < new_pages.length; i++) {
                this.facebook.pages.push(new_pages[i])
            }
        },
        updateFacebookUsers (new_users) {
            for (let i=0; i < new_users.length; i++) {
                this.facebook.users.push(new_users[i])
            }
        },
        updateFacebookGroups (new_groups) {
            for (let i=0; i < new_groups.length; i++) {
                this.facebook.groups.push(new_groups[i])
            }
        },
        loadAllFacebookAccounts () {
            return new Promise((resolve, reject) => {
                this.getConnectedFacebookAccounts()
                    .then(response => {
                        for (let i =0; i < this.facebook.users.length; i++) {
                            // Load all the pages and groups for all facebook accounts connected
                            let currentUser = this.facebook.users[i]
                            Promise.all([this.getAccountPages(currentUser.id).catch(error => error.response),
                                this.getAccountGroups(currentUser.id).catch(error => error.response)
                            ])
                                .then(responses => {
                                    // If the iteration is on the last one, then resolve the promise
                                    if (i === this.facebook.users.length - 1) {
                                        resolve(responses)
                                    }
                                    navBarInstance.isLoading = false
                                })
                                .catch(errors => {
                                    reject(errors)
                                    navBarInstance.isLoading = false
                                })
                        }
                        if(this.facebook.users.length === 0) {
                            resolve()
                            navBarInstance.isLoading = false
                        }
                    })
            })
        },
        searchLocation () {
            if(this.location.name !== '') {
                // If the name is not empty, then empty the latitude and longitude, if it's a current location request,
                // the name is auto emptied in the setCurrentLocationFromGPS
                this.location.lat = ''
                this.location.lng = ''
            }

            return new Promise(resolve => {
                this.locationSearch.isLoading = true
                HTTPClient.get(place_search_url + '?lat=' + this.location.lat + '&lng='
                    + this.location.lng + '&q=' + this.location.name)
                    .then(response => {
                        this.locationSearch.isLoading = false
                        this.locationSearch.results = response.data.data
                        resolve(response)
                    })
                    .catch(error => {
                        this.locationSearch.isLoading = false
                    })
            })
        },
        setCurrentLocationFromGPS () {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(position => {
                    this.location.lat = position.coords.latitude
                    this.location.lng = position.coords.longitude
                    // If we are using the user location, then clear the text in box
                    this.location.name = ''
                    this.searchLocation()
                }, error => {

                }, {enableHighAccuracy: true});
            } else {
                this.location.error = "Geolocation is not supported by this browser.";
            }
        },
        handleLocationSelect (location) {
            this.currentLocation = location
            UIkit.dropdown('#map-dropdown').hide()
        },
        downloadPostsCSV (posts) {
            let csv = 'ID,Message,Picture,Likes,Comments,Date\n';

            for (let i=0; i<posts.length; i++) {
                csv += posts[i].id + ',' + posts[i].message || '' + ',' + posts[i].picture + ',' +
                    posts[i].likes.summary.total_count + ',' + posts[i].comments.summary.total_count + ','
                    + posts[i].created_time
                csv += '\n'
            }
            let hiddenElement = document.createElement('a');
            hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
            hiddenElement.target = '_blank';
            hiddenElement.download = 'Exported Facebook Posts('+ moment(new Date()).toString() +').csv';
            hiddenElement.click();
        },
    }
}
