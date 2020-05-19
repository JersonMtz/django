from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
def get_directory(instance, filename):                             #Metodo para obtener el nombre del usuario
    old = Profile.objects.get(pk = instance.pk)                    #obtenemos la intancia actual
    old.avatar.delete()                                            #se elimina la img     
    return 'profile/'+ instance.user.username + '/' + filename    #luego crear su directorio para guardar la img


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to= get_directory, null=True, blank=True) 
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']


@receiver(post_save, sender = User)                                    #decorador que activa funcion cuando se crea una  instancia
def ensure_profile_exits(sender, instance, **kwargs):
    if(kwargs.get('created'), False):
        Profile.objects.get_or_create(user = instance)
        #print('Usuario creado')