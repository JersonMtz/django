from django.urls import path
from Apps.Messenger.views import ListMessagesView, DetailMessagesView, send_message_inbox, chat_init

Messenger_patterns = ([
    path('', ListMessagesView.as_view(), name='list'),
    path('<int:pk>/chat/', DetailMessagesView.as_view(), name='detail'),
    path('<int:pk>/inbox/', send_message_inbox, name='sms'),
    path('<username>/inbox/', chat_init, name='chat-new')
],'urlMessenger')

#le cambiamos el nombre de urlpatterns a cualquiera, se convierte en tupla y se asigna un nombre