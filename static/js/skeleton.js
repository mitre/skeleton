function toggleButtons() {
    $('#set1').toggle();
    $('#set2').toggle();
}

function enableButton(){
    validateFormState(true, '#uploadFile');
}

function doSomething(){
    restRequest('POST', {'index':'do_something'}, displayOutput, '/plugin/skeleton/api');
}

function uploadFile(){
    $('#fileInput').trigger('click');
}

$('#fileInput').on('change', function (event){
        if(event.currentTarget) {
            let filename = event.currentTarget.files[0].name;
            if(filename){
                restPostFile(event.currentTarget.files[0], function (data) {processFile(filename);})
                event.currentTarget.value = '';
            }
        }
});

function processFile(filename){
    let data = {'index': 'process_file',
                'option': $('#initialOptions').val(),
                'filename': filename
                }
    restRequest('POST', data, displayOutput, '/plugin/skeleton/api');
}

function restPostFile(file, callback=null, endpoint='/plugin/skeleton/upload'){
    let fd = new FormData();
    fd.append('file', file);
    $.ajax({
         type: 'POST',
         url: endpoint,
         data: fd,
         processData: false,
         contentType: false,
         success: function(data, status, options) {
            if(callback) {
                callback(data);
            }
            else {
                stream("successfully uploaded " + file.name);
            }
         },
         error: function (xhr, ajaxOptions, thrownError) {
             stream(thrownError);
         }
    });
}

function displayOutput(data){
    let results = data;
    document.getElementById("dataDisplay").value += results.output + '\n'
}