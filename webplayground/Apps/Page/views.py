from django.contrib.admin.views.decorators import staff_member_required       #import para verificar el staff
from django.utils.decorators import method_decorator                    #import para los decoradores
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from Apps.Page.models import *
from Apps.Page.forms import *


#el nombre de cada clase inicia con el nombre de la APP
#@method_decorator(staff_member_required, name='dispatch')       #decorador para restringir vista
class PagesListView(ListView):
    model = Pages

#@method_decorator(staff_member_required, name='dispatch')       #decorador para restringir vista
class PagesDetailView(DetailView):
    model = Pages

@method_decorator(staff_member_required, name='dispatch')        #decorador para restringir vista
class PagesCreate(SuccessMessageMixin, CreateView):
    model = Pages                                                #atributo de esta clase
    form_class = FormPages                                       #este es un atributo de clase propio, el form que creamos lo igualamos 
    success_url = reverse_lazy('urlPage:list')

    success_message = '%(title)s guardado correctamente' 

@method_decorator(staff_member_required, name='dispatch')              #decorador para restringir vista
class PagesUpdate(SuccessMessageMixin, UpdateView):
    model = Pages
    form_class = FormPages
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('urlPage:edit',args=[self.object.id])

    success_message = '%(title)s actualizado correctamente'


@method_decorator(staff_member_required, name='dispatch')              #decorador para restringir vista
class PagesDelete(SuccessMessageMixin, DeleteView):
    model = Pages
    success_url = reverse_lazy('urlPage:list')

    success_message = 'Se elimino correctamente'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)          #sobreescritura de la clase padre para eenviar sms de notificacion
        return super(PagesDelete, self).delete(request, *args, **kwargs)

