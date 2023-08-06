let VNRecorder, AudioStream;
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia || navigator.msGetUserMedia

const closeModal = (el_id) => {
    UIkit.modal(`#${el_id}`).hide()
}

const createCampaign = new Vue({
    el: '#campaign_form',
    delimiters: ["[[", "]]"],
    data: {
        campaign: {
            use_voice: false,
            use_email: false,
            use_mms: false,
            use_sms: false,
        }, // This is the remote campaign object created by the server
        errors: {},
        teams: [],
        phones: [],
        selected_logo_url: '',

        // Extras for follow up
        parent_campaign: parent_campaign,
        is_follow_up: !!is_follow_up
    },
    computed: {
        instance_id (){
            // Returns the campaign_id, if is in edit page
            return document.querySelector('#campaign_form').getAttribute('data-campaign_id')
        },
        getCampaignLogo () {
            return this.campaign.logo ? this.campaign.logo : ''
        }
    },
    methods: {
        openChannelsModal () {
            UIkit.modal("#addChannel").show();
        },
        get_url () {
            return this.campaign.id ? `/api/marketing/campaigns/${this.campaign.id}/` : `/api/marketing/campaigns/`
        },
        request (...args) {
            // If the campaign has been created before, then patch the existing created. Else create a new one
            // HTTPClient is from the base.html, it already carries the CSRFToken
            return !this.campaign.id ? HTTPClient.post(...args) :  HTTPClient.patch(...args)
        },
        next () {
            this.handleCampaignForm().then(r => this.openChannelsModal())
        },
        handleCampaignForm () {
            this.errors = {}
            let data = new FormData(this.$el)

            data.append('use_email', this.campaign.use_email)
            data.append('use_sms', this.campaign.use_sms)
            data.append('use_mms', this.campaign.use_mms)
            data.append('use_voice', this.campaign.use_voice)

            // If follow up campaign, add the following
            if (this.is_follow_up) {
                data.append('is_follow_up', true)
                data.append('parent_campaign', this.parent_campaign)
            }

            if (data.get('logo').size === 0) {
                //If a logo was not submitted, delete logo from data to be submitted
                data.delete('logo')
            }

            return new Promise((resolve, reject) => {
                this.request(this.get_url(), data)
                    .then(resp => {
                        this.campaign = resp.data
                        document.querySelector('#campaign_form').reset()
                        // Work around for uploading on every save, let vue re-update the other fields, the target is the file field
                        resolve(resp)
                    })
                    .catch(error => {
                        this.errors = error.response.data
                        notify('Campaign could not be saved!', 'danger')
                        reject(error)
                    })
            })
        },
        CompleteCampaignCreate () {
            // Save campaign again incase of edits, then redirect
            this.handleCampaignForm().then(r => window.location.href = '/marketing/campaigns/')
        },
        loadTeams () {
            HTTPClient.get('/api/marketing/teams/?page_size=200')
                .then(response => this.teams = response.data)
        },
        loadPhones () {
            let url = this.instance_id ? '/api/marketing/available-phone-numbers/?campaign=' + this.instance_id :
                '/api/marketing/available-phone-numbers/'
            HTTPClient.get(url)
                .then(response => this.phones = response.data.results)
        },
        loadCampaign () {
            return new Promise((resolve, reject) => {
                HTTPClient.get(this.$el.action)
                    .then(response => {
                        this.campaign = response.data
                        // If the schedule instance is loaded, it loads only in followup, then populate followup details
                        schedule ? schedule.loadFollowupDetails(this.campaign.follow_up_details) : null
                        resolve(response)
                    })
            })
        }
    },
    mounted () {
        if (this.instance_id) this.loadCampaign() // If it is an edit operation, preload campaign
        this.loadPhones()
        this.loadTeams()
    }
})

const channelsMixin = {
    data () {
        return {
            // to the form
            errors: {},
            attachment: '',
            campaign: {}, // This is the object returned by the server on create, it could be an  SMS, MMS, Voice, EMail campaign

            copy: '',
            test_error: '',

            fillInFields: [
                {key: '{{contact__phone}}', value: 'Phone number'},
                {key: '{{contact__first_name}}', value: 'first name'},
                {key: '{{contact__last_name}}', value: 'last name'},
                {key: '{{contact__email}}', value: 'email address'},
                {key: '{{contact__company_name}}', value: 'company name'},
                {key: '{{contact__designation}}', value: 'designation'},
            ],
            createCampaign: {
                title: '',
                campaign: '',
                phone_id: '',
                greeting_text: '',
                last_message: '',
                audio: '',
                voice_greeting_original: {}
            },
            isRecording: false,
            voice_note_src_url: null,
            isCreating: false,
            max_sms_char_count: 1585
        }
    },
    computed: {
        hasCreated () {
            return !!this.campaign.id
        },
        charLeft () {
            let length = this.campaign.text ? this.campaign.text.length : 0
            return this.max_sms_char_count - length
        },
        smsCount () {
            let length = this.campaign.text ? this.campaign.text.length : 0
            return Math.ceil(length / 145)
        }
    },
    methods: {
        get_url (campaign_type) {
            // If the campaign has been created once and the user still goes to the modal to make changes, then provide
            // an update url
            return !this.hasCreated ?
                `/api/marketing/campaigns/${createCampaign.campaign.id}/${campaign_type}/` :
                `/api/marketing/campaigns/${createCampaign.campaign.id}/${campaign_type}/${this.campaign.id}/`
        },
        request (...args) {
            // If the campaign has been created before, then patch the existing created. Else create a new one
            // HTTPClient is from the base.html, it already carries the CSRFToken
            return !this.hasCreated ? HTTPClient.post(...args) :  HTTPClient.patch(...args)
        },
        handleMediaChange (e) {
            this.attachment = e.target.files[0].name
        },
        handleCreateForm (data, campaign_type) {
            // This method handles form submission for the voice, sms, mms, email campaigns
            this.errors = {}
            data.append('campaign', createCampaign.campaign.id) // Add the created campaign's ID to the payload
            this.isCreating = true
            return new Promise((resolve, reject) => {
                this.request(this.get_url(campaign_type), data)
                    .then(response => {
                        this.isCreating = false
                        this.campaign = response.data
                        notify('Campaign has been saved!')
                        resolve(response)
                    })
                    .catch(error => {
                        this.isCreating = false
                        this.errors = error.response.data
                        notify('Error occurred saving campaign', 'danger')
                        reject(error)
                    })
            })
        },
        loadInitial (campaign_type) {
            return new Promise ((res, rej) => {
                if (createCampaign.instance_id) {
                    /*i.e if it is an edit operation*/
                    HTTPClient.get(`/api/marketing/campaigns/${createCampaign.instance_id}/${campaign_type}/`)
                        .then(resp => {
                            this.campaign = resp.data.results.length > 0 ? resp.data.results[0] : this.campaign
                            res(resp.data.results[0])
                        })
                }
                else {
                    res()
                }
            })
        },
        copyPasteInitChanged (event) {
            this.copy = event.target.value
        },
        handleTestCampaign (campaign_id, type, payload) {
            return new Promise((res, rej) => {
                HTTPClient.post(`/api/marketing/campaigns/${campaign_id}/${type}/test_campaign/`, payload)
                    .then(response => {
                        res(response)
                    })
                    .catch(error => {
                        rej(error)
                    })
            })
        }
    },
}

const campaignDelayMixin = {
    data () {
        return {
            delayTypes: {
                '0': 'Immediately',
                '1': 'Days',
                '2': 'Hours',
                '3': 'Minutes',
                '4': 'Seconds',
                '5': 'Specific Date'
            }
        }
    },
    computed: {
        delayTypeCanEnterDuration () {
            let delay_type = this.campaign.delay_type || '0'
            return [1, 2, 3, 4].includes(parseInt(delay_type, 10)) // Check if the delay type requires entering the duration integer
        },
        delayTypeIsDateScheduled () {
            let delay_type = this.campaign.delay_type || '0'
            return parseInt(delay_type, 10) === 5
        },
        delay_type: {
            set (val) {
                Vue.set(this.campaign, 'delay_type', val)
            },
            get () {
                let alt = this.campaign.trigger_date ? '5' : '0'
                return this.campaign.delay_type || alt
            }
        },
        delay_value: {
            set (val) {
                Vue.set(this.campaign, 'delay_value', val)
            },
            get () {
                return this.campaign.delay_value || null
            }
        },
        trigger_date: {
            set (val) {
                Vue.set(this.campaign, 'trigger_date', val)
            },
            get () {
                return this.campaign.trigger_date || null
            }
        }
    },
    watch: {
        delay_type (newValue) {
            if (parseInt(newValue, 10) === 5) {
                setTimeout(_ => {
                    initFlatPickerInstances()
                }, 400)
                // this.delay_value = null
            }
            // else {
            //     this.trigger_date = null
            // }
            //
            // if (!parseInt(newValue, 10)) { // If 'Immediately' is selected
            //     this.trigger_date = null
            //     this.delay_value = null
            // }
        }
    },
    methods: {
        setSendAt (event) {
            this.trigger_date = event.target.value
        }
    },
    mounted () {
        initFlatPickerInstances()
    }
}


const voice_form = new Vue({
    el: '#voice_form',
    delimiters: ["[[", "]]"],
    mixins: [channelsMixin, campaignDelayMixin],
    data: {
        ...additional_from_server,
    },
    methods: {

        openUploadCampaignVN(event) {
            document.querySelector('#audio').click();
            this.campaign.voice_to_text = null;
            this.voice_note_src_url = null;
        },

        blobToFile (blob, fileName) {
            blob = new File([blob], fileName)
            blob.lastModifiedDate = new Date();
            return blob;
        },
        resetVoiceNoteFileInput () {
            const input = document.querySelector('#audio')

            input.value = ''

            if(!/safari/i.test(navigator.userAgent)){
                input.type = ''
                input.type = 'file'
            }
        },
        startRecordingVN(event) {
            this.isRecording = true
            this.createCampaign.voice_note = null
            this.voice_note_src_url = null
            this.campaign.voice_greeting_original = null
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
                        this.campaign.audio = this.campaign.voice_greeting_original = this.blobToFile(voice_note_recording_blob, 'new_recording.wav')
                        this.attachment = true;
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
            this.campaign.audio = this.campaign.voice_greeting_original = event.target.files[0];
            this.attachment = true;
        },
        handleVoiceForm (event) {
            const form = event ? event.target : this.$el
            const data = new FormData(form)

            this.test_error = null
            this.errors = {}
            // if no new file is attached, then remove the audio attribute from from data to avoid replacing an
            // existing audio
            if (!this.attachment && !this.campaign.voice_to_text) {
                data.delete('audio')
            } else if (this.campaign.audio && !this.campaign.voice_to_text) {
                data.append('audio', this.campaign.audio)
            }
            this.handleCreateForm(data, 'voice').then(r => {closeModal('VoiceModal')})
        },
        RemoveAudioFile() {
            const that = this
            UIkit.modal.confirm('Are you sure you want to remove this file ?', {stack:true})
                .then(() => {
                    that.attachment = that.voice_note_src_url = that.campaign.audio = that.campaign.voice_greeting_original = null;
                    return new Promise(resolve => {
                        HTTPClient.get(this.campaign.remove_file_link)
                            .then(response => {
                                resolve(response)
                                that.attachment = that.voice_note_src_url = that.campaign.audio = that.campaign.voice_greeting_original = null;
                            })
                            .catch(error => {
                                console.log(error)
                            })
                    })
                })
        },
        handleTestVoice () {
            this.test_error = null
            this.errors = {}
            const test_data = new FormData(this.$el)
            if ((!this.attachment && !this.campaign.voice_to_text) || typeof test_data.get('audio') === 'object') {
                test_data.delete('audio')
            } else if (typeof this.campaign.audio === 'object' && !this.campaign.voice_to_text) {
                test_data.append('audio', this.campaign.audio)
            }
            // Extra or different data needed for testing
            test_data.append('phone', createCampaign.campaign.phone)
            test_data.append('greeting_text', test_data.get('voice_to_text'))
            if (test_data.get('audio')) {
                test_data.append('voice_greeting_original', test_data.get('audio'))
            }

            this.handleTestCampaign(createCampaign.campaign.id, 'voice', test_data)
                .then(response => {
                    if (response.data.error) {
                        this.test_eror = response.data.error
                    }
                    else {
                        UIkit.modal.dialog('<p class="uk-modal-body">Test Voice has been sent to ' +
                            test_data.get('sample_phone') + ' successfully!</p>', {stack:true});                    }
                })
                .catch(error => {
                    this.errors = error.response.data
                })
        },
    },
    mounted () {
        this.loadInitial('voice')
    }
})

const mms_form = new Vue({
    el: '#MMSModalForm',
    delimiters: ["[[", "]]"],
    mixins: [channelsMixin, campaignDelayMixin],
    data: {
    },
    methods: {
        handleMMSForm (event) {
            const data = new FormData(event.target)
            this.test_error = null
            this.errors = {}

            data.append('image1', data.get('image'))

            for (let key of data.keys()) {
                console.log(key, data.get(key))
            }

            // If no new image is attached, remove the image attributes from fields submitted
            if (!this.attachment) {
                data.delete('image')
                data.delete('image1')
            }

            this.handleCreateForm(data, 'mms').then(r => closeModal('MMSModal'))
        },
        handleTestMMS () {
            this.test_error = null
            this.errors = {}

            const test_data = new FormData(this.$el)

            // Extra or different data needed for testing
            test_data.append('image1', test_data.get('image'))

            this.handleTestCampaign(createCampaign.campaign.id, 'mms', test_data)
                .then(response => {
                    if (response.data.error) {
                        this.test_error = response.data.error
                    }
                    else {
                        UIkit.modal.dialog('<p class="uk-modal-body">Test MMS has been sent to ' +
                            test_data.get('sample_no') + ' successfully!</p>', {stack:true});                    }
                })
                .catch(error => {
                    this.errors = error.response.data
                })
        },
        RemoveMMSFile(field) {
            UIkit.modal.confirm('Are you sure you want to remove this file ?', {stack:true})
                .then(() => {
                    if (field === 'image1') {
                        this.attachment = null
                    }
                    this.campaign[field] = null
                    HTTPClient.get(this.campaign.remove_file_link + '?field=' + field)
                        .then(response => {
                        })
                        .catch(error => {
                            console.log(error)
                        })
                })
        },
    },
    mounted () {
        this.loadInitial('mms')
    }
})

const email_form = new Vue({
    el: '#EmailModalForm',
    delimiters: ["[[", "]]"],
    mixins: [channelsMixin, campaignDelayMixin],
    data: {
        body: '',
        email_template_id: '',
        email_type: 'basic'
    },
    computed: {
        shouldSendSample () {
            return !!this.campaign.email_for_sample
        },
        is_basic () {
            return this.email_type === 'basic'
        },
        email_body: {
            get () {
                return !!this.body ? this.body : this.campaign.body
            },
            set (value) {
                this.body = value
                this.campaign.body = value
            }
        }

    },
    methods: {
        openComposeEmailModal () {
            initializeEmailEditor(this.email_body)
            UIkit.modal('#newemailModal').show()
        },
        validateEmailForm () {
            // We'll add extra checks here
            return true
        },
        // handleEmailTypeChange (event) {
        //     this.campaign.email_type = event.target.value
        // },
        handleEmailForm (event) {
            this.test_error = null
            this.errors = {}

            if (this.validateEmailForm()) {
                const form = event ? event.target : this.$el
                const data = new FormData(form)

                data.append('body', this.email_body)

                if (this.email_template_id) {
                    if (data.get('email_type') === 'basic') {
                        data.append('template', this.email_template_id)
                    }
                    else {
                        data.append('premium_template', this.email_template_id)
                    }
                }

                return new Promise (resolve => {
                    this.handleCreateForm(data, 'email')
                        .then(r => {
                            if (event) {
                                // If event, means it was submitted not tested
                                closeModal('emailModal')
                            }
                            resolve(r.data) // Resolve campaign
                        })
                })
            }
        },
        handleEmailTest () {
            this.test_error = null
            this.errors = {}

            let test_data = new FormData(this.$el)
            test_data.append('sample_email_for_email', this.campaign.email_for_sample)
            test_data.append('body', this.email_body)

            if (this.email_template_id) {
                if (test_data.get('email_type') === 'basic') {
                    test_data.append('template', this.email_template_id)
                }
                else {
                    test_data.append('premium_email_template', this.email_template_id)
                }
            }

            this.handleTestCampaign(createCampaign.campaign.id, 'email', test_data)
                .then(response => {
                    if (response.data.error) {
                        this.test_error = response.data.error
                    }
                    else {
                        UIkit.modal.dialog('<p class="uk-modal-body">Test Email has been sent to ' +
                            test_data.get('email_for_sample') + ' successfully!</p>', {stack:true});
                    }
                })
                .catch(error => {
                    this.errors = error.response.data
                })
        }
    },
    mounted () {
        this.loadInitial('email')
            .then(data => {
                if (data) {
                    this.email_template_id = data.template
                    this.email_type = data.email_type
                }
            })
    }
})

const sms_form = new Vue({
    el: '#SMSModalForm',
    delimiters: ["[[", "]]"],
    mixins: [channelsMixin, campaignDelayMixin],
    data: {
        max_sms_char_count: 1585
    },
    computed: {
        charLeft () {
            let length = this.campaign.text ? this.campaign.text.length : 0
            return this.max_sms_char_count - length
        },
        smsCount () {
            let length = this.campaign.text ? this.campaign.text.length : 0
            return Math.ceil(length / 145)
        }
    },
    methods: {
        handleSMSForm (event) {
            this.test_error = null
            this.errors = {}
            const data = new FormData(event.target)
            this.handleCreateForm(data, 'sms').then(r => closeModal('SMSModal'))
        },
        handleTestSMS () {
            this.test_error = null
            this.errors = {}

            const test_data = new FormData(this.$el)

            this.handleTestCampaign(createCampaign.campaign.id, 'sms', test_data)
                .then(response => {
                    if (response.data.error) {
                        this.test_error = response.data.error
                    }
                    else {
                        UIkit.modal.dialog('<p class="uk-modal-body">Test SMS has been sent to ' +
                            test_data.get('sample_no') + ' successfully!</p>', {stack:true});
                    }
                })
                .catch(error => {
                    this.errors = error.response.data
                })
        }
    },
    mounted () {
        this.loadInitial('sms')
    }
})

const composeEmailModal = new Vue({
    el:'#newemailModal',
    delimiters: ['[[', ']]'],
    data: {
        email_body: email_form.email_body
    },
    methods: {
        handleEmailBodyComposeComplete () {
            // Set the email body written to the Email vue model object, then hide the compose modal
            const value = CKEDITOR.instances.editor1.getData()
            email_form.email_body = value
            email_form.body = value
            UIkit.modal('#newemailModal').hide()
        }
    },
})

const chooseEmailTemplateModal = new Vue({
    el: '#emailtempModal',
    delimiters: ["[[", "]]"],
    data: {
        templates: {},
        premium_templates: {},
        recommended_templates: {},
        selected_template_: null,
        selected_premium_template_: null,
        showPremiumRefresh: false
    },
    computed: {
        selected_template: {
            set (newValue) {
                this.selected_template_ = newValue
            },
            get () {
                if (this.selected_template_) return this.selected_template_
                else {
                    if (email_form.campaign.email_type === 'basic') {
                        return email_form.campaign.template
                    }
                    else {
                        return ''
                    }
                }
            }
        },
        selected_premium_template: {
            set (newValue) {
                this.selected_premium_template_ = newValue
            },
            get () {
                if (this.selected_premium_template_) return this.selected_premium_template_
                else {
                    if (email_form.campaign.email_type === 'premium') {
                        return email_form.campaign.premium_template
                    }
                    else {
                        return ''
                    }
                }
            }
        },
        email_type_is_basic () {
            return email_form.is_basic
        }
    },
    watch: {
        selected_template (newValue) {
            email_form.email_template_id = newValue
            email_form.campaign.template = newValue
        },
        selected_premium_template (newValue) {
            email_form.email_template_id = newValue
            email_form.campaign.template = newValue
        }
    },
    methods: {
        loadTemplates () {
            HTTPClient.get('/api/marketing/emailtemplates/')
                .then(response => this.templates = response.data)
        },
        loadPremiumTemplates () {
            HTTPClient.get('/api/marketing/emailtemplates/?premium=true')
                .then(response => this.premium_templates = response.data)
        },
        loadRecommendedTemplates () {
            HTTPClient.get('/api/marketing/emailtemplates/?recommended=true')
                .then(response => this.recommended_templates = response.data)
        },
        closeChoose () {
            closeModal('emailtempModal')
        },
        openCreateNewTemplate () {
            this.showPremiumRefresh = true
            window.open('/template/design/email/', '_blank', 'menubar=0,location=0,width=800')
        },
        refreshTemplatesOnSignal (event) {
            if (event.isTrusted && event.key === 'template-save') {
                window.localStorage.removeItem('template-save') // remove so it'll trigger a change on the next set
                this.loadPremiumTemplates()
            }
        },
        listenToStorageForTemplateSave () {
            window.addEventListener('storage', this.refreshTemplatesOnSignal)
        }
    },
    mounted () {
        this.loadTemplates()
        this.loadPremiumTemplates()
        this.loadRecommendedTemplates()
        this.listenToStorageForTemplateSave()
    },
    unmounted () {
        window.removeEventListener('storage', this.refreshTemplatesOnSignal)
    }
})

const channelModal = new Vue({
    el: '#addChannel',
    delimiters: ['[[', ']]'],
    computed: {
        hasVoice () {
            return !!voice_form.campaign.id
        },
        hasMMS () {
            return !!mms_form.campaign.id
        },
        hasSMS () {
            return !!sms_form.campaign.id
        },
        hasEmail () {
            return !!email_form.campaign.id
        },
        noChannelHasBeenFilled () {
            return !voice_form.campaign.id && !mms_form.campaign.id && !sms_form.campaign.id && !email_form.campaign.id
        },
        use_email: {
            get () {
                return createCampaign.campaign.use_email
            },
            set (value) {
                createCampaign.campaign.use_email = value
            }
        },
        use_sms: {
            get () {
                return createCampaign.campaign.use_sms
            },
            set (value) {
                createCampaign.campaign.use_sms = value
            }
        },
        use_mms: {
            get () {
                return createCampaign.campaign.use_mms
            },
            set (value) {
                createCampaign.campaign.use_mms = value
            }
        },
        use_voice: {
            get () {
                return createCampaign.campaign.use_voice
            },
            set (value) {
                createCampaign.campaign.use_voice = value
            }
        },
        schedule_type () {
            return schedule.schedule_
        }
    },
    methods: {
        confirmAtLeastOneChannelIsFilled () {
            let test = this.hasSMS + this.hasVoice + this.hasEmail + this.hasMMS
            return new Promise((resolve, reject) => {
                if (test < 1) {
                    reject()
                    UIkit.modal.alert('Please fill in at least one of the channels', {stack: true})
                }
                else {
                    resolve()
                }
            })
        },
        confirmAtLeastOneChannelIsTurnedOn () {
            let test = (this.use_voice * this.hasVoice) + (this.use_sms * this.hasSMS) +
                (this.use_mms * this.hasMMS) + (this.use_email * this.hasEmail)
            return new Promise((resolve, reject) => {
                if (test < 1) {
                    reject()
                    UIkit.modal.alert('Please toggle on at least one of the filled channels', {stack: true})
                }
                else {
                    resolve()
                }
            })
        },
        openTriggerModal () {
            createCampaign.handleCampaignForm() // Save the campaign again
            this.confirmAtLeastOneChannelIsFilled()
                .then(r => this.confirmAtLeastOneChannelIsTurnedOn())
                .then(r => UIkit.modal('#triggerCampaignModal').show())
        },
        closeChannelsModal () {
            createCampaign.handleCampaignForm() // Save the campaign again
            window.location.href = '/marketing/campaigns/'
        },
        openScheduleModal () {
            createCampaign.handleCampaignForm() // Save the campaign again
            this.confirmAtLeastOneChannelIsFilled()
                .then(r => this.confirmAtLeastOneChannelIsTurnedOn())
                .then(r =>
                    UIkit.modal('#schedule-campaign').show()
                )
        }
    }
})

const triggerCampaign = new Vue({
    el: '#triggerCampaignModal',
    delimiters: ['[[', ']]'],
    data: {
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
            campaigns: {
                is_selected: false,
                all: [],
                selected: []
            }
        },
        triggerLoading: false,
        triggerComplete: false
    },
    computed: {

    },
    methods: {
        loadContacts () {
            HTTPClient.get('/api/contacts/?page_size=200')
                .then(response => this.categories.contacts.all = response.data.results)
        },
        loadGroups () {
            HTTPClient.get('/api/group/?page_size=200')
                .then(response => this.categories.groups.all = response.data.results)
        },
        loadCampaigns () {
            HTTPClient.get('/api/marketing/campaigns/?page_size=200')
                .then(response => this.categories.campaigns.all = response.data.results)
        },
        groupsChanged (event) {
            console.log(event.target)
        },
        triggerCampaign () {
            this.triggerLoading = true
            let payload = {
                groups: this.categories.groups.is_selected ? this.categories.groups.selected : [],
                contacts: this.categories.contacts.is_selected ? this.categories.contacts.selected : [],
                campaigns: this.categories.campaigns.is_selected ? this.categories.campaigns.selected : []
            }
            HTTPClient.post('/api/marketing/campaigns/' + createCampaign.campaign.id + '/trigger/', payload)
                .then(response => {
                    this.triggerLoading = false
                    this.triggerComplete = true
                    UIkit.modal.dialog('<p class="uk-modal-body">Yaay! 💃 Campaign ' +
                        createCampaign.campaign.name + ' has been triggered successfully! 👌</p>', {stack:true});
                })
                .catch(error => {
                    this.triggerLoading = false
                    notify('Error occurred while triggering campaign!', 'danger')
                })
        },
        selectForTrigger (value, type) {
            this.categories[type].selected.push(value)
        },
        removeFromTrigger (value, type) {
            let index = this.categories[type].selected.findIndex(val => val)
            this.categories[type].selected.splice(index, 1)
        }
    },
    mounted () {
        this.loadContacts()
        this.loadGroups()
        this.loadCampaigns()
    }
})


const schedule = document.querySelector('#schedule-campaign') ? new Vue({
    el: '#schedule-campaign',
    delimiters: ['[[', ']]'],
    computed: {
        schedule_: {
            set (value) {
                createCampaign.campaign.follow_up_details.schedule_type = value
                this.schedule = value
            },
            get () {
                let sch;
                let fup = createCampaign.campaign.follow_up_details
                if (createCampaign.campaign.follow_up_details) {
                    this.schedule_types.map(value => value.key === fup.schedule_type ? sch = value : null)
                }
                let alt = this.schedule ? this.schedule : ""
                return sch || alt
            }
        }
    },
    watch: {
        schedule_ (newValue) {
            this.follow_up_details.custom = false
            this.follow_up_details.onleadcapture = false
            this.follow_up_details.recur = false
            this.follow_up_details.specific = false
            this.follow_up_details.now4leads = false
            Vue.set(this.follow_up_details, newValue.key, true)
        }
    },
    data: {
        schedule_types: [
            {
                key: 'onleadcapture',
                value: 'Immediately lead is captured',
                hint: 'When a lead is captured, this will be sent out instantly'
            },
            {
                key: 'custom',
                value: 'Custom Schedule',
                hint: 'This will be sent to your leads after the duration you specify, relative to their capture date and time'
            },
            {
                key: 'now4leads',
                value: 'Send to existing leads',
                hint: 'This will be sent instantly to all your existing leads'
            },
            {
                key: 'recur',
                value: 'Recurring',
                hint: 'This will be sent periodically in the intervals you specify either day or hours to you existing leads at that particular time'
            },
            {
                key: 'specific',
                value: 'Specific Date/Time',
                hint: 'This will be sent on the date and time you specify, to leads in this campaign'
            },
        ],
        schedule: null,
        follow_up_details: {
            recur_interval: 0,
            recur_interval_unit: '1',
            sp_date: null,
            custom_delay: 0,
            custom_delay_unit: '1',
            custom: false,
            onleadcapture: false,
            now4leads: false,
            recur: false,
            specific: false
        },
        delayTypes: {
            '1': 'Days',
            '2': 'Hours',
            '3': 'Minutes',
            '4': 'Seconds',
        },
        isSaving: false,
        errors: {}
    },
    methods: {
        loadFollowupDetails (follow_up_details) {
            this.follow_up_details = follow_up_details
        },
        sp_date_changed (event) {
            this.follow_up_details.sp_date = event.target.value
        },
        saveSchedule () {
            this.errors = {}
            this.isSaving = true
            let app = createCampaign
            this.follow_up_details.sp_date = new Date(this.follow_up_details.sp_date).toISOString()
            let extra_payload = {follow_up_details: this.follow_up_details}
            this.schedule_types.forEach(value => extra_payload.follow_up_details[value.key] = (value.key === this.schedule_.key))
            let payload = Object.assign({}, app.campaign, extra_payload) // Merge campaign data and the follow up details
            delete payload['logo'] // this attribute cannot go in JSON, would throw validation error from the server
            app.request(app.get_url(), payload)
                .then(response => {
                    notify('Follow up campaign has been saved', 'success', 2000)
                    setTimeout(() => {
                        window.location.href = '/marketing/campaigns/'
                    }, 1500)
                })
                .catch(error => {
                    this.isSaving = false
                    this.errors = error.response.data
                    notify(error.message, 'danger', 1500)
                })
        }
    },
    mounted () {
    }
}) : null
