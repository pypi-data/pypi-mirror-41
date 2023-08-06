function openCommand(cmdUrl) {
    // if (REQUEST_RUNNING) {
    //     return false;
    // }

    let formDiv = document.getElementById('form-div');
    fetch(cmdUrl)
        .then(function(response) {
            return response.text();
        })
        .then(function(theFormHtml) {
            formDiv.innerHTML = theFormHtml;
        });
}
