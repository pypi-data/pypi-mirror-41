let VNRecorder, AudioStream;
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia || navigator.msGetUserMedia

const surveyFilterMixin = {
    data () {
        return  {
            filter_values: {
                title: '',
                campaign: '',
                phone: '',
                created: ''
            },
            engaged_numbers: {
                results: [],
            },
            showFilters: true
        }
    },
    methods: {
        filterSurveys () {
            this.getAllSurveys('/api/marketing/surveys/?' + dictToURLArgs(this.filter_values))
        },
        clearFilters () {
            this.filter_values = {
                title: '',
                campaign: '',
                phone: '',
                created: ''
            }
            this.getAllSurveys()
        },
        getAllEngagedPhoneNumbers () {
            HTTPClient.get('/api/marketing/engaged-phone-numbers/?engaged_by=survey')
                .then(response => {
                    this.engaged_numbers = response.data
                })
        }
    },
    mounted () {
        this.getAllEngagedPhoneNumbers ()
    }
}

let trigger_mixin = {
    data () {
        return {
            categories: {
                contacts: {
                    is_selected: false,
                    all: [],
                    selected: []
                },
                groups: {
                    is_selected: false,
                    all: [],
                    selected: []
                },
            },
            triggerLoading: false,
            survey_to_trigger: null
        }
    },
    methods: {
        loadContacts () {
            HTTPClient.get('/api/contacts/?page_size=1000')
                .then(response => this.categories.contacts.all = response.data.results)
        },
        loadGroups () {
            HTTPClient.get('/api/group/?page_size=1000')
                .then(response => this.categories.groups.all = response.data.results)
        },
        openTrigger (survey_id) {
            UIkit.modal('#trigger-survey-modal').show()
            this.survey_to_trigger = survey_id
            this.loadContacts()
            this.loadGroups()
        },
        selectForTrigger (value, type) {
            this.categories[type].selected.push(value)
        },
        removeFromTrigger (value, type) {
            let index = this.categories[type].selected.findIndex(val => val)
            this.categories[type].selected.splice(index, 1)
        },
        triggerSurvey () {
            this.triggerLoading = true
            this.errors = {}
            let payload = {
                groups: this.categories.groups.is_selected ? this.categories.groups.selected : [],
                contacts: this.categories.contacts.is_selected ? this.categories.contacts.selected : [],
            }
            HTTPClient.post('/api/marketing/surveys/' + this.survey_to_trigger + '/trigger/', payload)
                .then(resp => {
                    this.triggerLoading = false
                    UIkit.modal.dialog('<p class="uk-modal-body">Yaay! 💃 Survey has been triggered successfully! 👌</p>', {stack:true});
                })
                .catch(error => {
                    this.triggerLoading = false
                    this.errors = error.response.data
                    notify('Error triggering survey', 'danger')
                })
        },
    }
}

const surveys = new Vue({
    el: '#surveys',
    delimiters: ["[[", "]]"],
    mixins: [surveyFilterMixin, trigger_mixin],
    data: {
        surveys: {
            count: 0,
            next: null,
            previous: null,
            results: []
        },
        surveyToBeCreated: {
            title: '',
            campaign: '',
            phone_id: '',
            greeting_text: '',
            last_message: '',
            voice_greeting_original: null
        },
        showArchived: false,
        availablePhones: {
            count: 0,
            next: null,
            previous: null,
            results: []
        },
        campaigns: {
            count: 0,
            next: null,
            previous: null,
            results: []
        },
        surveyToEdit: {
            id: '',
            title: '',
            campaign: '',
            phone_id: '',
            greeting_text: '',
            last_message: '',
            voice_greeting_original: null
        },
        surveyToEdit_phone_id: '',
        errors: {},
        filter_values: {

        },
        //Trigger
        contacts: [],
        groups: [],

        // Recording data
        isRecording: false,
        voice_note_src_url: null,

        //pagination
        page: 0
    },
    computed: {
        unarchivedSurveys () {
            return this.surveys.results.filter(survey => survey.active === true)
        },
        archivedSurveys () {
            return this.surveys.results.filter(survey => survey.active === false)
        },
    },
    methods: {
        openCreateSurvey () {
            this.getAvailablePhoneNumbers();
            UIkit.modal("#create-survey-modal").show();

        },
        openEditSurveyModal (survey_id) {
            /*Open modal edit survey and prepopulated the survey data*/
            this.resetCreateEditSurvey()

            this.getSurvey(survey_id)
                .then(survey => {

                    this.surveyToEdit = survey;

                    const modalEditSurvey = UIkit.modal("#edit-survey-modal");
                    this.surveyToEdit_phone_id = survey.phone ? survey.phone.id : survey.phone; // Set phone preselected.
                    this.voice_note_src_url = survey.voice

                    modalEditSurvey.show();
                    this.getAvailablePhoneNumbers();

                })
                .catch(err => {
                    // Integrate front errors with sentry or other #TODO
                    console.log(err);
                    notify('Error occured!')
                });

        },
        resetCreateEditSurvey () {
            this.surveyToEdit = {
                id: '',
                title: '',
                campaign: '',
                phone_id: '',
                greeting_text: '',
                last_message: '',
                voice_greeting_original: null
            }
            this.surveyToBeCreated = {
                title: '',
                campaign: '',
                phone_id: '',
                greeting_text: '',
                last_message: '',
                voice_greeting_original: null
            }

            this.voice_note_src_url = null

        },
        updateSurvey (survey_id) {
            // if (this.surveyToEdit_phone_id) {
            //     this.surveyToEdit.phone_id = this.surveyToEdit_phone_id;
            // }

            this.errors = {}
            let data = new FormData()

            for (let key in this.surveyToEdit) {
                if (this.surveyToEdit.hasOwnProperty(key)) {
                    let value = this.surveyToEdit[key]
                    // If no voice note file is attached, don't append it
                    if (key === 'voice_greeting_original') {
                        if (value !== null && value) {
                            data.append(key, value)
                        }
                    }
                    else if (key === 'campaign') {
                        if (value) {
                            data.append(key, value)
                        }
                    }
                    else {
                        data.append(key, value)
                    }
                }
            }

            HTTPClient.patch('/api/marketing/surveys/' + survey_id + '/', data)
                .then(response => {

                    UIkit.modal("#edit-survey-modal").hide();
                    this.getAllSurveys();

                }).catch(err => {
                this.errors = err.response.data
                console.log(err);
            });
        },
        getSurvey (survey_id) {
            /**
             * Returns survey by ID
             */
            return HTTPClient.get('/api/marketing/surveys/' + survey_id + '/')
                .then(response => {
                    return response.data;
                })
                .catch(err => {
                    console.log(err);
                });

        },
        createSurvey () {
            this.errors = {}
            let data = new FormData()

            for (let key in this.surveyToBeCreated) {
                if (this.surveyToBeCreated.hasOwnProperty(key)) {
                    let value = this.surveyToBeCreated[key]
                    if (key === 'voice_greeting_original') {
                        if (value !== null && value) {
                            data.append(key, value)
                        }
                    }
                    else {
                        data.append(key, value)
                    }
                }
            }

            HTTPClient.post('/api/marketing/surveys/', data)
                .then(response => {
                    UIkit.modal("#create-survey-modal").hide();
                    this.surveys.results.unshift(response.data)
                    this.resetCreateEditSurvey()
                    this.getAllEngagedPhoneNumbers()
                })
                .catch(err => {
                    this.errors = err.response.data
                    console.log(err);
                });
        },
        archive: function (id, url) {
            HTTPClient.get(url)
                .then(response => {
                    let index = this.surveys.results.findIndex(s => s.id === id)
                    this.surveys.results.splice(index, 1)
                    this.surveys.results.unshift(response.data)
                    this.showArchived = true
                }).catch(err => {
                notify('Error occurred archiving survey')
            });
        },
        unarchive (id, url) {
            HTTPClient.get(url)
                .then(response => {
                    let index = this.surveys.results.findIndex(s => s.id === id)
                    this.surveys.results.splice(index, 1)
                    this.surveys.results.unshift(response.data)
                }).catch(err => {
                notify('Error occurred unarchiving survey')
            });
        },
        getAvailablePhoneNumbers: function () {
            /*
            * Returns the available phone numbers
            * The URL is gotten based on the parameter, if no parameter is supplied, then it's a complete reload,
            * else it is a previous or next request
            * For next page, call function like this "getAvailablePhoneNumbers('next')", for previous, call function
            * like this "getAvailablePhoneNumbers('previous')"
            * */
            let url = this.surveyToEdit.id ? '/api/marketing/available-phone-numbers/?survey='+this.surveyToEdit.id : '/api/marketing/available-phone-numbers/'

            return HTTPClient.get(url)
                .then(response => {
                    this.availablePhones = response.data
                })
                .catch(err => {
                    console.log(err);
                });

        },
        getAllSurveys: function (url) {
            const url_ = url ? url : '/api/marketing/surveys/';
            HTTPClient.get(url_)
                .then(response => {
                    this.surveys = response.data
                })
                .catch(error => {
                    notify('Error occurred loading surveys!')
                })
            // this.getActiveSurveys(action);
            // this.getArchivedSurveys(action);
        },
        getAllCampaigns () {
            HTTPClient.get('/api/marketing/campaigns/')
                .then(response => this.campaigns = response.data)
                .catch(err => console.log(err));
        },
        openUploadSurveyVN(event) {
            document.querySelector('#surveyVN').click();
        },
        voice_note_change(event) {
            // Delete the current recording if the user has recorded already
            this.voice_note_src_url = null
            this.surveyToBeCreated.voice_greeting_original = event.target.files[0];
            this.surveyToEdit.voice_greeting_original = event.target.files[0];
        },
        blobToFile (blob, fileName) {
            blob = new File([blob], fileName)
            blob.lastModifiedDate = new Date();
            return blob;
        },
        resetVoiceNoteFileInput () {
            const input = document.querySelector('#surveyVN')

            input.value = ''

            if(!/safari/i.test(navigator.userAgent)){
                input.type = ''
                input.type = 'file'
            }
        },
        startRecordingVN(event) {
            this.isRecording = true
            this.surveyToBeCreated.voice_note = null
            this.voice_note_src_url = null

            // Empty the file input if the user has uploaded a file already, since we can only use one
            this.resetVoiceNoteFileInput()

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
                        this.surveyToBeCreated.voice_greeting_original = this.blobToFile(voice_note_recording_blob, 'new_recording.wav')
                        this.surveyToEdit.voice_greeting_original = this.blobToFile(voice_note_recording_blob, 'new_recording.wav')
                    })
                })
                .catch(error => {
                    console.log(error)
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
        toggleTreeSurveyQuestions (event, key) {
            console.log(event.target.value)
            let target_survey = this.surveys.results[key]
            if (!target_survey.questions) {
                HTTPClient.get('/api/marketing/surveys/' + target_survey.id + '/questions/')
                    .then(response => {
                        Vue.set(target_survey, 'questions', response.data)
                    })
            }
        },
        loadAnswerChildQuestions (payload) {
            let index = payload.index
            let choice = payload.choice

            console.log(payload)

            HTTPClient.get('/api/marketing/surveys/questions/answer-options/' + choice.id + '/questions/')
                .then(response => {
                    choice.questions = response.data
                })
                .catch(error => {

                })
        },
        next () {
            this.page++
            this.getAllSurveys(this.surveys.next)
        },
        previous () {
            this.page--
            this.getAllSurveys(this.surveys.previous)
        }
    },
    mounted() {
        this.getAllCampaigns();
        this.getAllSurveys();
        this.getAvailablePhoneNumbers();
    }
});

