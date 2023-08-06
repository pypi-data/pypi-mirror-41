let VNRecorder, AudioStream;
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia || navigator.msGetUserMedia

let personalizedMixin = {
    data () {
        return {
            messages: {
                results: [],
                next: null,
                previous: null,
                count: 0
            },
            isRecording: false,
            voice_note_src_url: null,
            audio_channel: '0',
            //pagination
            page: 0,
            message: {
                name: '',
                type: 'voice',
                audio: '',
                text: ''
            },
            context_fields: [
                {key: '{{contact__phone}}', value: 'Phone number'},
                {key: '{{contact__first_name}}', value: 'first name'},
                {key: '{{contact__last_name}}', value: 'last name'},
                {key: '{{contact__email}}', value: 'email address'},
                {key: '{{contact__company_name}}', value: 'company name'},
                {key: '{{contact__designation}}', value: 'designation'},
            ],
            currentContextValue: '',
            errors: {}
        }
    },
    watch: {
        message: {
            handler (newValue) {
                if (newValue.type === 'sms') {
                    this.message.audio = ''
                    this.voice_note_src_url = null
                }
            },
            deep: true
        },
        audio_channel (newVal) {
            this.message.audio = ''
            this.message.text = ''
        }
    },
    computed: {

    },
    methods: {
        loadMessages (url) {
            let url_ = url ? url : '/api/marketing/autodialer/personalized-messages/'
            HTTPClient.get(url_)
                .then(resp => {
                    this.messages = resp.data
                })
                .catch(error => {
                    notify('Error loading personalized messages', 'danger')
                })
        },
        deleteMessage (index, id) {
            UIkit.modal.confirm('Are you sure you want to remove this message ?')
                .then(r => {
                    HTTPClient.delete('/api/marketing/autodialer/personalized-messages/' + id + '/')
                        .then(resp => {
                            this.messages.results.splice(index, 1)
                        })
                })
        },
        handleCreateMessage () {
            this.errors = {}
            let data = Object.assign({}, this.message)
            HTTPClient.post('/api/marketing/autodialer/personalized-messages/', dictToFormData(data))
                .then(resp => {
                    this.messages.results.unshift(resp.data)
                    this.message = {
                        name: '',
                        type: 'voice',
                        audio: '',
                        text: ''
                    }
                    if (document.querySelector('#MessageModal')) {
                        UIkit.modal('#MessageModal').hide()
                    }
                    if (this.refreshMessages) {
                        this.refreshMessages()
                    }
                    notify('Message has been added!')
                })
                .catch(error => {
                    console.log(error)
                    this.errors = error.response.data
                    notify('Error occured Creating Messages', 'danger')
                })
        },
        openCreateMessageModal () {
            UIkit.modal('#MessageModal').show()
        },
        openUploadMessage(event) {
            document.querySelector('#audio').click();
            this.message.text = '';
            this.voice_note_src_url = null;
        },
        messageTypeChanged (event) {
            this.message.type = event.target.value
        },
        blobToFile (blob, fileName) {
            blob = new File([blob], fileName)
            blob.lastModifiedDate = new Date();
            return blob;
        },
        startRecordingVN(event) {
            this.isRecording = true
            this.voice_note_src_url = null

            navigator.mediaDevices.getUserMedia({audio: true})
                .then(stream => {
                    AudioStream = stream
                    VNRecorder = new MediaRecorder(stream)
                    VNRecorder.start()

                    const audioChunks = []
                    VNRecorder.addEventListener('dataavailable', event => {
                        audioChunks.push(event.data)
                    })

                    VNRecorder.addEventListener('stop', () => {
                        let voice_note_recording_blob = new Blob(audioChunks, { 'type' : 'audio/wav; codecs=MS_PCM' })
                        // Construct URL for the recorded audio so we can listen
                        this.voice_note_src_url = URL.createObjectURL(voice_note_recording_blob)
                        // Create the file from the recording and set to the survey object
                        this.message.audio = this.blobToFile(voice_note_recording_blob, 'new_recording.wav')
                        this.message.text = ''
                    })
                })
                .catch(error => {
                    alert('No device found for this operation!')
                    this.isRecording = false
                })
        },
        stopRecording() {
            VNRecorder.stop()
            // Adding the setTimeout to give time for slow devices to render the player after recording
            if (document.querySelector('#vn_player')) {
                document.querySelector('#vn_player').play()
            }
            else {
                setTimeout(() => {
                    document.querySelector('#vn_player').play()
                }, 500)
            }

            AudioStream.getTracks()[0].stop()
            this.isRecording = false
        },
        voice_note_change(event) {
            // Delete the current recording if the user has recorded already
            this.voice_note_src_url = null
            this.message.audio = event.target.files[0];
        },
        RemoveAudioFile () {
            this.message.audio = ''
            this.voice_note_src_url = null
        },
        next () {
            this.loadMessages(this.messages.next)
            this.page++
        },
        previous () {
            this.loadMessages(this.messages.previous)
            this.page--
        }
    },
    mounted () {
        this.loadMessages()
    }
}

let perEl = document.querySelector('#personalized')

const personalized = perEl ? new Vue({
    el: '#personalized',
    delimiters: ['[[', ']]'],
    mixins: [personalizedMixin],
}) : null
