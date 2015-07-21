// var gapi = null;

function init() {
    var api_root = '//' + window.location.host + '/_ah/api';
    console.log(api_root);

    gapi.client.load('wordsapi', 'v1', function() {
        console.log('wordsapi is loaded');
//        get_words_api(4, 'yslmwklgnsig');
    }, api_root);
}

function get_words_api(length, letters){
    gapi.client.wordsapi.words.get({'length': length, 'choices': letters}).execute(function(resp){
        console.log(resp);
    });
}

$(document).ready(function(){
    $('#submit').on('click', function(e){
//        e.preventDefault();
        console.log('call the endpoint api');
    });
});

