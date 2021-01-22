$('#sheet-form').submit(function( event ) {
    $('#form-warning').hide();
    $('#form-success').hide();
    var sheet = {
        "name": $('#name').val(),
        "type": $('#type').val(),
        "tier": $.isNumeric($('#tier').val()) ? parseInt($('#tier').val()) : 0,
        "might": $.isNumeric($('#might').val()) ? parseInt($('#might').val()) : 0,
        "speed": $.isNumeric($('#speed').val()) ? parseInt($('#speed').val()) : 0,
        "intellect": $.isNumeric($('#intellect').val()) ? parseInt($('#intellect').val()) : 0,
        "effort": $.isNumeric($('#effort').val()) ? parseInt($('#effort').val()) : 0,
        "edge": {
            "intellect": $.isNumeric($('#edgeintellect').val()) ? parseInt($('#edgeintellect').val()) : 0,
            "might": $.isNumeric($('#edgemight').val()) ? parseInt($('#edgemight').val()) : 0,
            "speed": $.isNumeric($('#edgespeed').val()) ? parseInt($('#edgespeed').val()) : 0
        },
        "abilities": [],
        "equipment": $('#equipment').val().split("\n"),
        "skills": {}
    };
    console.log(sheet);
    $('input[name="abilities[]"]:checked').each(function(){
        sheet.abilities.push($(this).val());
    });

    var skill_list = $('#skill-list').val().split("\n");
    for(var i = 0; i < skill_list.length; i++) {
        var val = $(`input:radio[name=skill-${skill_list[i]}]:checked`).val()
        if(parseInt(val) != 0) {
            sheet.skills[skill_list[i]] = val
        }
    }
    console.log(sheet);

    try {
        $.ajax({
            url: '/api/v1/characters',
            type: 'POST',
            data: JSON.stringify(sheet),
            dataType: 'json',
            contentType: "application/json"
        }).always(function(data, textStatus, jqXHR) {
            console.log(JSON.stringify(data));
            if(jqXHR.status == 201) {
                $('#form-success').html(
                    'Your character parameters can be viewed at this URL:<br>'+
                    `<a href="${data.api}">${data.api}</a><br>`+
                    'Print that page (or save the URL) and bring it with you to session zero for character creation.');
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
    
    event.preventDefault();
  });