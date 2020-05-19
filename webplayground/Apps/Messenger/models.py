from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

#clase para personalizar (Hereda de model.Manager)
class ThreadManager(models.Manager):
    def find(self, userOne, userTwo):
        queryset = self.filter(users = userOne).filter(users = userTwo)       #Es igual a decir *Thread.objects*
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, userOne, userTwo):
        thread = self.find(userOne, userTwo)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(userOne, userTwo)
        return thread

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='thread')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)   #se fuerza el guardado en la señal para almacenar la fecha

    objects = ThreadManager()   #se agrega la clase para personalizar las consultas

    class Meta:
        ordering = ['-updated']     #se ordena de forma inversa con **-** y el campo


#Validacion para evitar mensajes de terceros#
def validation_message(sender, **kwargs):
    #obtener los valores del **kwargs
    instance = kwargs.pop('instance', None)             #instancia del objeto (Thread)
    action = kwargs.pop('action', None)                 #acción del proceso
    pk_set = kwargs.pop('pk_set', None)                 #IDs involucrados en el proceso

    temp_pk = set()                                     #una variable falsa temporal para la suplantación

    if action == 'pre_add':                             #si la acción es pre agregar... ejecute
        for pk_sms in pk_set:                           #recorro el arreglo de IDs involucrados
            sms = Message.objects.get(pk=pk_sms)        #obtengo el registro de Message con el IDs involucrados
            if sms.user not in instance.users.all():    #si el user no esta en la instancia creada
                print('{} está infiltrado'.format(sms.user))    #mensaje depuración
                temp_pk.add(pk_sms)                             #agrego a la varible temp el ID del user infiltrado
    
    pk_set.difference_update(temp_pk)                           #Con este metodo quita de pk_set el mensaje infriltrado

    instance.save()                                             #se forzo el guardado en el campo updated

m2m_changed.connect(validation_message, sender=Thread.messages.through) #se conceta la señal con el campo del modelo