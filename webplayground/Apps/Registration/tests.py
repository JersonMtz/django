from django.test import TestCase
from Apps.Registration.models import Profile
from django.contrib.auth.models import User

# Create your tests here. (para ejecutar en consola usar ** python manage.py test  'NOMBRE APP o RUTA' **)

''' Este archivo test funciona para testear 
el funcionamiento de algunos procesos o de la app'''

class ProfileCreateTest(TestCase):
    def setUp(self):
        User.objects.create_user('prueba', 'prueba@mail.com', 'prueba1425')     #creamos una instancia del modelo USER

    def test_profile_exists(self):                                              #creamos la funcion con la palabra de primero 'test'
        exists = Profile.objects.filter(user__username='prueba').exists()       #filtramos el objeto para comprobar que existe
        self.assertEqual(exists, True)                                          #de esta clase ejecutamos el test, y Si o Si comparamos