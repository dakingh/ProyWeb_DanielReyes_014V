//validacion formulario contactanos
//validando inicio de sesion
$(function(){
    $("#inicio-sesion").validate({
        rules:{
            usuario:{
                required:true,
                email:true
            },
            password:{
                required:true
            }
        },
        messages:{
            usuario:{
                required:'Ingrese correo electronico',
                email:'Ingrese un email valido'
            },
            password:{
                required:'Ingrese una contraseña valida',
                minlength: 'Digitos insuficientes',
                maxlength:'Contraseña demaciado larga!!'
            }
        },
        submitHandler: function(form) {
            alert("Inicio de sesión correctamente");
            form.submit();
        }
    });//fin inicio de sesion
    //validando registro de usuarios
    $("#registro-usuario").validate({
        rules:{
            nombre:{
                required:true
            },
            apellidos:{
                required:true
            },
            direccion:{
                required:true
            },
            telefono:{
                required:true,
                number:true
            },
            comuna:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            pass1:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:'#pass1'
            }
        },
        messages:{
            nombre:{
                required:'Ingrese su nombre',
                minlength:'Caracteres insuficientes..(3)',
                maxlength:'Demaciados caracteres!!'
            },
            apellidos:{
                required:'Ingrese su apellido',
                minlength:'Caracteres insuficientes..(5)',
                maxlength:'Demaciados caracteres!!'
            },
            direccion:{
                required:'Ingrese su direccion',
                minlength:'Caracteres insuficientes..(4)',
                maxlength:'Demaciados caracteres!!'
            },
            telefono:{
                required:'Ingrese su numero de telefono',
                number:'Telefono invalido',
                minlength:'Digitos insuficientes..(9)',
                maxlength:'Numero de telefono invalido!!'
            },
            comuna:{
                required:'Ingrese comuna',
                minlength:'Digitos insuficientes..(5)',
                maxlength:'Demaciados caracteres!!'
            },
            correo:{
                required:'Ingrese correo electronico',
                email:'Formato de correo invalido!!'
            },
            pass1:{
                required:'Ingrese su contraseña..',
                minlength:'Caracteres insuficientes'
            },
            pass2:{
                required:'Reingrese su contraseña',
                minlength:'Caracteres insuficientes',
                equalTo:'Contraseñas no coinciden'
            }
        },
        submitHandler: function(form) {
            alert("Registro de usuario exitoso");
            form.submit();
        }
    })
});//fin registro de usuario

