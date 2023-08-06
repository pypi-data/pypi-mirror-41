/**
 * Twilio Client configuration for the browser-calls-django
 * example application.
 */
const TwilioMixin = {
    data () {
        return {
            call_status : 'Initializing...',
            in_call: false,
            is_ringing: false,
            outgoing_recipient: '',

            // For answering call, we assign this so we can accept through it with the accept button
            connection: null,
            duration: 0,
            timer: null,
            isMute: false
        }
    },
    computed: {
        getDuration () {
            let mins = (parseInt(this.duration / 60, 10)).toString()
            let seconds = (this.duration % 60).toString()
            mins = mins.length > 1 ? mins : ('0' + mins)
            seconds = seconds.length > 1 ? seconds : ('0' + seconds)
            return mins  + ':' + seconds
        }
    },
    watch: {
        isMute (newValue) {
            this.connection.mute(newValue)
        }
    },
    methods: {
        initTwilio () {
            HTTPClient.get('/api/marketing/autodialer/dial/get_token/', {forPage: window.location.pathname})
                .then(response => {
                    Twilio.Device.setup(response.data.token, {debug:true})

                    Twilio.Device.ready(device => {
                        this.call_status = 'Ready'
                    });

                    /* Report any errors to the call status display */
                    Twilio.Device.error(error => {
                        this.call_status = 'Error: ' + error.message
                        if (error.code === 31205) { // If the token is expired
                            window.location.reload()
                        }
                        //TODO: Check if the twilio client has encountered an error , if the error is due to network issue, pause the autodialer

                    });

                    this.listenDeviceConnect()
                    this.listenDeviceDisconnect()
                    this.listenIncomingCall()
                })
        },
        listenDeviceDisconnect () {
            /* Callback for when a call ends */
            Twilio.Device.disconnect(connection => {
                this.call_status = "Ready";
                this.connection = null;
                this.outgoing_recipient = ''
                if (this.autoDialingInProgress && typeof this.autoDialPosition === 'number') {
                    if (this.startCountdown) {
                        this.startCountdown()
                    }
                    let app = this
                    setTimeout(() => {
                        if (!app.autoDialingPaused) {
                            app.autoDialPosition += 1
                        }
                    }, this.callInterval * 1000)
                }
                UIkit.modal('#callingModal').hide()
            });
        },
        listenDeviceConnect () {
            Twilio.Device.connect(connection => {
                this.in_call = true
                this.connection = connection
                this.startTimer()
                UIkit.modal('#callingModal').show()

                // If phoneNumber is part of the connection, this is a call from a
                // support agent to a customer's phone
                if ("PhoneNumber" in connection.message) {
                    this.call_status = "In call with " + connection.message.PhoneNumber;
                } else {
                    // This is a call from a website user to a support agent
                    this.call_status = "In call with support";
                }
            });
        },
        listenIncomingCall () {
            Twilio.Device.incoming(connection => {
                this.call_status = "Incoming support call";
                this.is_ringing = true

                UIkit.modal('#callingModal').show()

                // Set a callback to be executed when the connection is accepted
                connection.accept(() => {
                    this.call_status = "In call with customer";
                });

                this.connection = connection

            });
        },
        answerPhone() {
            this.connection.accept()
            this.is_ringing = false
        },
        callCustomer (to, from) {
            this.call_status = 'Calling Customer ' + to + '...'
            this.outgoing_recipient = to
            let params = {"PhoneNumber": to, "from_no": from};
            Twilio.Device.connect(params);
        },
        callBackFromCampaign (to, from) {
            this.call_status = 'Calling ' + to + '...'
            let params = {"PhoneNumber": to, "from_no": from};
            Twilio.Device.connect(params);
        },
        callSupport () {
            Twilio.Device.connect();
        },
        hangUp () {
            this.in_call = false
            Twilio.Device.disconnectAll();
            this.stopTimer()
        },
        rejectCall () {
            this.connection.reject()
            this.is_ringing = false
        },
        toggleMute () {
            this.isMute = !this.isMute
        },
        startTimer () {
            this.timer = setInterval(this.updateDuration, 1000)
        },
        stopTimer () {
            clearInterval(this.timer)
            this.duration = 0
        },
        modalToggleListener () {
            let app = this
            UIkit.util.on('#callingModal', 'hide', function () {
                if (app.connection) {
                    document.querySelector('#floating-call').classList.remove('uk-hidden')
                }
                else {
                    document.querySelector('#floating-call').classList.add('uk-hidden')
                }
            })
            UIkit.util.on('#callingModal', 'show', function () {
                document.querySelector('#floating-call').classList.add('uk-hidden')
            })
        },
        expandCall () {
            UIkit.modal('#callingModal').show()
        },
        updateDuration () {
            this.duration += 1
        }
    },
    mounted () {
        this.initTwilio()
        this.modalToggleListener()
    }
}
