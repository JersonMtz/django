$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

/** cuando carga la pagina muestro los mensajes **/
window.onload = function(){
    var txt = document.getElementById('txt'); //obtengo si existe ese elemento
    if ( txt != null) {
        const Toast = Swal.mixin({
            toast: true,
            position: 'top',
            showConfirmButton: false,
            timer: 5000,
            timerProgressBar: true,
            onOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer),
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        });
        Toast.fire({icon:'success',title: txt.getAttribute('data-sms')})    //envio el mensaje en la notificación
        txt.remove();                                                       //remuevo el elemento para no *perjudicar
    }
}

const form = document.getElementById('form-delete');                        //Guardo el unico form del HTML
const list = document.getElementsByClassName('delete');                     //objento el array de botones eliminar

//Recorro cada boton en busca evento click para ejecutar la consulta
for (const item of list) {
    item.addEventListener('click', function(evt){
        evt.preventDefault();                                               //detengo el comportamiento del elemento
        Swal.fire({
            title: '¡Atención!',
            html: "¿Esta seguro que desea eliminar <b>"+ this.getAttribute('data-title') +'</b>?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#17A2B8',
            cancelButtonColor: '#888888',
            confirmButtonText: 'Aceptar'
        }).then((result) => {
            if (result.value) {
                form.action = this.href;    //paso la url para eliminar al form
                form.submit();              //envio el form para confirmar la eliminación
            }
        })
    });
}
