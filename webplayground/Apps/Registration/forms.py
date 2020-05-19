from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Apps.Registration.models import Profile
import os

class UserCreationFormEmail(UserCreationForm):
    first_name = forms.CharField(required=True, help_text="Campo requerido, 30 carácteres máximo")
    last_name = forms.CharField(required=True, help_text="Campo requerido, 150 carácteres máximo")
    email = forms.EmailField(required=True, help_text="Campo requerido, 254 carácteres máximo.")

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email ya registrado.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'row':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }
    
    #Obtener los valores del formularios para validaciones
    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()         #obtengo el arreglo de datos
        if not cleaned_data['avatar'] and self.instance.avatar: #valido que NO halla foto y la instancia exista
            if os.path.isfile(self.instance.avatar.path):       #checar si la foto existe en la ruta
                self.instance.avatar.delete(False)              #ejecuto el metodo que elimina el archivo
        return cleaned_data                                     #retorno la nueva data

class ProfileEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Campo requerido, 254 carácteres máximo.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:                #si email esta en la lista de cambios
            if User.objects.filter(email = email).exists():
                raise forms.ValidationError('Email ya registrado, intente nuevamente')
        return email