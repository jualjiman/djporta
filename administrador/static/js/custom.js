$(document).ready(function(){
	$("#loading img").hide();
	$("#mainContent").fadeIn();
	
	setObjects();

    $("#btnSend").click(function(e){
        e.preventDefault();

         var name = $('#id_nombre').val();
         var email = $('#id_email').val();
         var message = $('#id_mensaje').val();

        if( name !== "" && email !== "" && message !== ""){
            $.ajax({
                type: "POST",
                url: "/contactame/",  // or just url: "/my-url/path/"
                data: {
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                    name: name,
                    email: email,
                    message: message
                },
                success: function(data) {
                    $('.alert-info').text('Mensaje enviado, Muchas gracias!').hide().fadeIn();
                },
                error: function(xhr, textStatus, errorThrown) {
                    $('.alert-danger').text('Error al enviar el mensaje.').hide().fadeIn();
                }
            });
        }
        else{
            $('.alert-warning').text('Todos los campos son requeridos').hide().fadeIn();
        }
    });
});


// $(document).on("click",".btnnb",function(e){
// 	var clss = $(this).attr("class");
// 	clsf = clss.substring(6);

// 	if(clsf == "b1")
// 	{
// 		$("#estu").hide();
// 		$("#proy").hide();
// 		$("#info").fadeIn();
// 	}
// 	else if(clsf == "b2")
// 	{
// 		$("#info").hide();
// 		$("#proy").hide();
// 		$("#estu").fadeIn();
// 	}
// 		else if(clsf == "b3")
// 	{
// 		$("#info").hide();
// 		$("#estu").hide();
// 		$("#proy").fadeIn();
// 	}
// });

