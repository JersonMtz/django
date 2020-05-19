from django.shortcuts import render
from django.views.generic.list import ListView
#from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from Apps.Messenger.models import Thread, Message
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required   #import pque se enviar para validar view solo logueado
from django.utils.decorators import method_decorator        #import para decorar las funciones

# Create your views here.
class DetailMessagesView(DetailView):
    template_name = 'Messenger/messages_detail.html'
    model = Thread

    #filtrar solo mensajes al cual pertenece, evitar ingreso por URL
    def get_object(self): #coorelativo a get_queryset
        obj = super(DetailMessagesView, self).get_object()      #se obtiene la consulta
        if self.request.user not in obj.users.all():
            raise Http404("Ud no puede acceder a este link")    #si user no esta en la conversación generamos un error 404
        return obj                                              #se retorna la data

@method_decorator(login_required, name='dispatch')              #se envia la funcion y el metodo a decorar "DISPACTH"
class ListMessagesView(ListView):
    template_name = 'Messenger/messages_list.html'
    model = Thread          #Se usa el model del hilo donde convergen la conversación de los usuarios

    def get_queryset(self):
        queryset = super(ListMessagesView, self).get_queryset()     #se obtiene la query de la consulta
        return queryset.filter(users = self.request.user)           #se devuelve solo el filtro de los sms del usuario identificado

def send_message_inbox(request, pk):
    txt = {'feeback': '','first': False}                                            #este será nuestra bandera
    if request.method == 'POST':
        if request.user.is_authenticated:
            message = request.POST['sms']
            if message:
                chat = get_object_or_404(Thread, pk=pk)                             #obtengo el hilo del chat
                mjs = Message.objects.create(user=request.user, content=message)    #creo un nuevo mensaje
                chat.messages.add(mjs)                                              #agrego el mensaje al chat
                txt['feeback'] = message

                #si es el primer mensaje
                if len(chat.messages.all()) is 1:
                    txt['first'] = True
        else:
            raise Http404('Usuario no identificado')
    else:
        txt['feeback'] = 'Método de envio modificado'
        
    return JsonResponse(txt)

@login_required                                            #valida que este logueado para ejecutarse
def chat_init(request, username):
    this_user = get_object_or_404(User, username=username)                      #obtenemos el usuario o generamos un 404
    new_chat = Thread.objects.find_or_create(this_user, request.user)           #buscamos o creamos un chat con el
    return redirect(reverse_lazy('urlMessenger:detail', args=[new_chat.pk]))    #usuario encontrado y el logueado
    #retornamos a la vista para iniciar conversación  con el id del chat en ARGS[]