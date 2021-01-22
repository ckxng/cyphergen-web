$('#setting-form').submit(function( event ) {
    $('#form-warning').hide();
    $('#form-success').hide();
    var setting;
    try {
        setting = $.parseJSON($('#setting-data').val());

        try {
            $.ajax({
                url: '/api/v1/games',
                type: 'POST',
                data: $('#setting-data').val(),
                dataType: 'json',
                contentType: "application/json; charset=utf-8"
            }).always(function(data, textStatus, jqXHR) {
                console.log(JSON.stringify(data));
                if(jqXHR.status == 201) {
                    $('#form-success').html(
                        'Character creation for your campaign is available at this URL:<br>'+
                        `<a href="${data.web}">${data.web}</a><br>`+
                        'Your submitted campaign parameters can be viewed '+
                        `<a href="${data.api}">here</a>.`);
                    $('#form-success').show();
                } else {
                    $('#form-warning').html("The server failed to process the request.  Check to make sure your input matches the template." );
                    $('#form-warning').show();
                }
            })
        } catch(error) {
            $('#form-warning').html("Failed to submit the form to the server."+error);
            $('#form-warning').show();
        }

    } catch(error) {
        $('#form-warning').html("Setting is not in valid JSON format.");
        $('#form-warning').show();
    }
    
    event.preventDefault();
  });