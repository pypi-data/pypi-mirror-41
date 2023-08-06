const register = new Vue({
    el: '#register',
    delimiters: ['[[', ']]'],
    data: {
        reg_data: {
            fullname: '',
            email: '',
            password: '',
            company: '',
            phone: '',
            tac: false
        },
        isError: false,
        errors: []
    },
    methods: {
        handleRegister () {
            this.isError = false
            this.errors = []
            let registrationForm = document.querySelector('#registrationForm')
            HTTPClient.post(registrationForm.action, new FormData(registrationForm))
                .then(response => {
                    if (response.data.success === 'true') {
                        window.location.href = '/user/register/success/'
                    }
                    else {
                        this.isError = true
                        this.errors.push(response.data.message)
                        window.scrollTo({top: 0, behavior: 'smooth'})
                    }
                })
                .catch(response => {

                })
        }
    },
    mounted () {

    }
})
