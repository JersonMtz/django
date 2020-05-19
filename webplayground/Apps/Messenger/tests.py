from django.test import TestCase
from Apps.Messenger.models import Thread, Message
from django.contrib.auth.models import User

# Create your tests here.

class ThreadTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user001', None, 'test1234')
        self.user2 = User.objects.create_user('user002', None, 'test1234')
        self.user3 = User.objects.create_user('user003', None, 'test1234')

        self.thread = Thread.objects.create()

    #Test de seguridad de invirtrado en la conversación
    def test_add_user_infiltration(self):
        self.thread.users.add(self.user1, self.user2)
        sms1 = Message.objects.create(user=self.user1, content="Hola user1")
        sms2 = Message.objects.create(user=self.user2, content="Hola user2")
        sms3 = Message.objects.create(user=self.user3, content="Hola user3")
        self.thread.messages.add(sms1, sms2, sms3)
        self.assertEqual(len(self.thread.messages.all()), 2)

    #Test para el uso de la funcion FIND de model.Maneger
    def test_find_users_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

    #Test para el uso de la funcion FIND de model.Maneger buscar o crear Hilo
    def test_find_or_create_thread(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

        self.thread.users.add(self.user2, self.user3)
        thread = Thread.objects.find_or_create(self.user2, self.user3)
        self.assertIsNotNone(thread)