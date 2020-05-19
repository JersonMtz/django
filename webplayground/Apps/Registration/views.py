from Apps.Registration.forms import UserCreationFormEmail, ProfileForm, ProfileEmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django import forms
from Apps.Registration.models import Profile

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationFormEmail
    template_name = 'Registration/signup.html'
    success_url = reverse_lazy('login')

    success_message = '%(first_name)s %(last_name)s registrado correctamente'
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        #modificar tiempo real
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Digite su nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Digite sus apellidos'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Digite su usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Digite su email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Confirme contraseña'})
        return form



@method_decorator(login_required, name = 'dispatch')
class ProfileUpdate(SuccessMessageMixin, UpdateView):
    template_name = "Registration/profile_form.html"
    model = Profile
    form_class = ProfileForm        
    success_url = reverse_lazy('urlRegistration:profile')

    success_message = 'Información de perfil actualizado'

    def get_object(self):
        #obtener el objeto para editar
        profile, created = Profile.objects.get_or_create(user = self.request.user) #retorna una tupla
        return profile



@method_decorator(login_required, name = 'dispatch')
class ProfileEmailUpdate(SuccessMessageMixin, UpdateView):
    form_class = ProfileEmailForm
    template_name = "Registration/profile_email_form.html"
    success_url = reverse_lazy('urlRegistration:profile')

    success_message = 'Email actualizado'

    def get_object(self):
        return self.request.user # recuperar user

    def get_form(self, form_class=None):
        form = super(ProfileEmailUpdate, self).get_form()
        #modificar tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Digite su email'})
        return form
