const SMMShared = {
    data: {
        errors: [],
        allAccountsMixed: [
            // List of all accounts mixed together not grouped
        ],
        location: {
            // These are the values the user enters or gotten from the user's current location
            name: '',
            lat: '',
            lng: '',
            error: ''
        },
        currentLocation: {
            //    This is the one from the platform on select by the user
        },
        locationSearch: {
            isLoading: false,
            results: []
        }
    },
    methods: {

    }
}