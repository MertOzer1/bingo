function eraseSheet(sheetId) {
    // Placeholder for erase logic
    alert('Erase Sheet ' + sheetId);
}

function confirmReset() {
    return confirm('Are you sure you want to start a new game? This will reset all called numbers.');
}

function confirmErase(sheetId) {
    if (confirm('Are you sure you want to erase this sheet?')) {
        var form = document.createElement('form');
        form.method = 'post';
        form.action = '/bingo/delete_sheet/' + sheetId + '/';

        // Retrieve CSRF Token from the hidden input
        var csrfToken = document.getElementById('csrfToken').value;
        var input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'csrfmiddlewaretoken';
        input.value = csrfToken;
        form.appendChild(input);

        document.body.appendChild(form);
        form.submit();
    }
}

