function signalToParentAndClose () {
    window.localStorage.setItem('template-save', true)
    setTimeout(function () {
        window.close()
    }, 500)
}

$(document).ready(function() {
    var request = function(method, url, data, type, callback) {
        var req = new XMLHttpRequest();
        req.onreadystatechange = function() {
            if (req.readyState === 4 && req.status === 200) {
                var response = JSON.parse(req.responseText);
                callback(response);
            }
        };

        req.open(method, url, true);
        if (data && type) {
            if(type === 'multipart/form-data') {
                var formData = new FormData();
                for (var key in data) {
                    formData.append(key, data[key]);
                }
                data = formData;
            }
            else {
                req.setRequestHeader('Content-type', type);
            }
        }
        req.send(data);
    };
    var save = function(filename, content) {
        saveAs(new Blob([content], {type: 'text/plain;charset=utf-8'}), filename);
    };

    var beeConfig = {
        uid: 'landing-page-designer',
        container: 'bee-plugin-container',
        autosave: 15,
        language: 'en-US',
        specialLinks: [],
        mergeTags: [],
        mergeContents: [],
        onSave: function(jsonFile, htmlFile) {
            UIkit.modal.confirm('Are you sure you want to save web template design!!')
                .then(() => {
                    var template_name = $('input[name=name]').val();
                    if(!template_name){
                        UIkit.modal.dialog('Please provide template name!')
                    } else {
                        $('.loader, .overlay').show();
                        $('input[name=json_data]').val(jsonFile);
                        $('input[name=email_body]').val(htmlFile);
                        $.post( $(this).attr('action'), $('form').serialize())
                            .done(function( data ) {
                                signalToParentAndClose()
                                // window.location.href = data.next_url;
                                $('.loader, .overlay').hide();
                            });
                    }
                })
        },
        onSaveAsTemplate: function(jsonFile) {
        },
        onAutoSave: function(jsonFile) { // + thumbnail?
            console.log(new Date().toISOString() + ' autosaving...');
            window.localStorage.setItem('newsletter.autosave', jsonFile);
        },
        onError: function(errorMessage) {
            console.log('onError ', errorMessage);
        }
    };
    request('POST', 'https://auth.getbee.io/apiauth', auth, 'application/x-www-form-urlencoded',
        function(token) {
            BeePlugin.create(token, beeConfig, function(beePluginInstance) {
                bee = beePluginInstance;
                bee.start(JSON.parse($('input[name=json_data]').val()));
            });
        });
});
