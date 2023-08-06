const forgot_password = new Vue({
    el: '#forgot-password',
    delimiters: ['[[', ']]'],
    data: {
        reset_data: {
            email: '',
        },
        isError: false,
        errors: []
    },
    methods: {
        handlePasswordReset () {
            this.isError = false
            this.errors = []
            let resetPasswordForm = document.querySelector('#resetPasswordForm')
            HTTPClient.post(resetPasswordForm.action, new FormData(resetPasswordForm))
                .then(response => {
                    if (response.data.success === 'true') {
                        window.location.href = '/user/reset-password-email/'
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
