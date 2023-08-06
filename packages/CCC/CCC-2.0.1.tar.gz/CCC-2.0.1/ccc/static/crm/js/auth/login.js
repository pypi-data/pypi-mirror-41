const login = new Vue({
    el: '#login',
    delimiters: ['[[', ']]'],
    data: {
        login_data: {
            email: '',
            password: '',
        },
        isError: false,
        errors: []
    },
    methods: {
        handleLogin () {
            this.isError = false
            this.errors = []
            let loginForm = document.querySelector('#loginForm')
            HTTPClient.post(loginForm.action, new FormData(loginForm))
                .then(response => {
                    if (response.data.success === 'true') {
                        if (response.data.redirect) {
                            window.location.href = response.data.redirect
                        }
                        else {
                            window.location.href = '/'
                        }
                    }
                    else {
                        this.isError = true
                        this.errors.push(response.data.message)
                    }
                })
                .catch(error => {

                })
        }
    },
    mounted () {

    }
})
