function init() {
    var api_root = '//' + window.location.host + '/_ah/api';
    console.log(api_root);

    gapi.client.load('wordsapi', 'v1', function() {
        console.log('wordsapi is loaded');
    }, api_root);
}
