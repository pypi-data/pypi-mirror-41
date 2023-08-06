const business_card = new Vue({
    el: '#business_card',
    delimiters: ["[[", "]]"],
    data: {
        digital_card: {
            file: {},
            social: null
        },
        contact_id: null
    },
    methods: {
        previewPhoto (event) {
        const that = this;
            this.digital_card.file = event.target.files[0]
            function readURL(input) {
                if (event.target.files && event.target.files[0]) {
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        $('#digital_card_image').attr('src', e.target.result);
                    }
                    reader.readAsDataURL(event.target.files[0]);
                }
            }
            readURL(event);
        },

        loadBusinessCard() {
            HTTPClient.get('/api/contacts/business_card/')
            .then(response => {
                this.contact_id = response.data.contact_id
                HTTPClient.get('/api/contacts/' + this.contact_id + '/')
                .then(response => $.extend(true, this.digital_card, response.data))
                    .catch(error => {
                        notify('Error occurred: ' + error.message)
                    })
                }
            )
            .catch(error => {
                notify('Error occurred: ' + error.message)
            })
        },
        saveBusinessCard (event) {
            const form = event ? event.target : this.$el
            const data = new FormData(form)
            data.append('contact_type', 'DBC')
            HTTPClient.patch('/api/contacts/' + this.contact_id + '/', data)
                .then(response => {
                    this.loadBusinessCard()
                    notify('Updated Business card')
                })
                .catch(error => {
                    notify('Error occurred: ' + error.message)
                })
        },
        loadMap () {
            function initMap() {
                var lat_log = {lat: 33.3048635, lng: -111.7883613};
                var map = new google.maps.Map(
                    document.getElementById('map'), {zoom: 12, center: lat_log});
                var marker = new google.maps.Marker({position: lat_log, map: map});
            }
        }
    },
    mounted () {
        this.loadBusinessCard()
        this.loadMap()
    }
});
