let croppie_ = null

const buyerProfile = new Vue({
    el: '#profile',
    delimiters: ['[[', ']]'],
    data: {
        profile_image: null,
        uploadedProfileImageURL: null,
        isUploading: false,
    },
    mixins: [subUsersMixin],
    computed: {

    },
    methods: {
        profileImageUpload ($event) {
            const files = $event.target.files
            if (files) {
                this.readFile($event.target)
            }
        },
        readFile(input) {
            let app = this
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    app.uploadedProfileImageURL = e.target.result
                    if (!croppie_) {
                        setTimeout(app.initCroppie, 250)
                    }
                    UIkit.modal('#crop-image-modal').show()
                }

                reader.readAsDataURL(input.files[0]);
            }
        },
        initCroppie () {
            croppie_ = new Croppie(document.getElementById('imageToCrop'), {
                viewport: { width: 200, height: 200 },
                boundary: { width: 300, height: 300 },
                enableOrientation: true
            })
        },
        submitProfileUpdateForm (profile_image) {
            return new Promise((resolve, reject) => {
                const formElement = document.querySelector('#profileform')
                const formData = new FormData(formElement)
                formData.set('profile_image', profile_image)
                HTTPClient.patch(updateUserAPI, formData)
                    .then(response => {
                        resolve(response)
                    })
                    .catch(error => {
                        reject(error)
                    })
            })
        },
        submitCroppedImage ($event) {
            this.isUploading = true
            croppie_.result('blob').then(profile_image_blob => {
                // convert the blob to image and set random name to the new file also
                const file_name = first_name ? first_name : Math.random().toString(36).substring(7)
                const newImageFile = new File([profile_image_blob], file_name + '.jpg');

                this.submitProfileUpdateForm(newImageFile)
                    .then(response => {
                        // De-initialize croppie
                        croppie_ = null
                        // Hide modal
                        UIkit.modal('#crop-image-modal').hide()
                        this.isUploading = false
                        // Reload Page
                        window.location.reload(true)
                    })
                    .catch(error => {
                        this.isUploading = false
                        notify('Error Uploading Photo:' + error.response.data || error.message)
                        console.log(error.response)
                    })
            });
        },
        closeCropWindow ($event) {
            croppie_ = null
            UIkit.modal('#crop-image-modal').hide()
        },
        getProfileImagePath () {
            return this.profile_image ? window.URL.createObjectURL(this.profile_image) : ''
        }
    },
    created () {

    }
})
