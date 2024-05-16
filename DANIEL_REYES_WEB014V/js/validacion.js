//validacion formulario contactanos
$(function(){
    $("#datos-contactos").validate({
        rules:{
            nom:{
                required:true
            },
            apellidos:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            telefono:{
                required:true,
                number:true
            },
            mensaje:{
                required:true
            }
        },
        messages:{
            nom:{
                required:'Ingrese su nombre',
                minlength:'Caracteres insuficientes..(3)'
            },
            apellidos:{
                required:'Ingrese su apellido',
                minlength:'Caracteres insuficientes..(3)'
            },
            correo:{
                required:'Ingrese su correo electronico',
                email:'Formato de correo invalido'
            },
            telefono:{
                required:'Ingrese su numero de telefono',
                number:'Telefono invalido',
                minlength:'Digitos insuficientes',
                maxlength:'Numero de telefono invalido!!'
            },
            mensaje:{
                required:'Ingrese el texto que desea enviar'
            }
        },
        submitHandler: function(form) {
            alert("Formulario enviado correctamente");
            form.submit();
        }
    });
});

