/** Metodos y acciones **/
document.getElementById('content').addEventListener('keyup', function(){
    if(!this.value || !this.checkValidity()){
        btn.disabled = true;
    } else {
        btn.disabled = false;
    }
});

function scrollChat(){
    const chat = document.getElementById('chat');
    chat.scrollTop = chat.scrollHeight;
}

scrollChat();
/***************/

/*** Agregar mensaje ***/
function newMessage(text){
    let element = document.createElement('div');
    element.classList.add('mine','mb-3');
    let new_message = '<div class="py-3">'+text+'</div><div class="card-footer d-block p-0"><div class="row"><div class="col-md-8"><small class="blockquote-footer"><cite>Tú</cite></small></div><div class="col-md-4"><small class="float-right text-muted"><i>Hace un momento</i></small><br></div></div></div>';
    element.innerHTML = new_message;
    document.getElementById('chat').appendChild(element);
    document.getElementById('content').value = '';
    btn.disabled = true;
    this.scrollChat();
}
/**** ***/

/***** Envio mensaje *****/
const btn = document.getElementById('send');
const token = document.querySelector('input[name=csrfmiddlewaretoken]').value;  // obtengo el token

btn.addEventListener('click', function(){
    let text = document.getElementById('content').value;
    if (text.length > 0){
        let message = new FormData();               // se crea un formData para guardar la data
        message.append('sms', text);                // se agrega el contenido con una clave
        
        fetch(this.getAttribute('data-url'),        //este metodo recibe la url y un JSON con las opciones
        {
            headers: { "X-CSRFToken": token },      //se agrega el token en el encabezado **nombre clave no debe cambiar**
            credentials: 'include',                 //incluyen las credenciales
            method: 'POST',                         //metodo de envio
            body: message                           //se envia el form data
        })
        .then(response => response.json())
        .then(function(data){                   // respuesta enviada desde el servidor
            if (data.first){
                window.location.reload(true);
            } else if (data.feeback) {
                this.newMessage(data.feeback);
            }
        });
    }
});

