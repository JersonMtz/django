from django.urls import path
from Apps.Page.views import *

Page_patterns = ([
    path('list/', PagesListView.as_view(), name='list'),
    path('detail/<int:pk>/<slug:slug>', PagesDetailView.as_view(), name='detail'),
    path('create/', PagesCreate.as_view(), name='create'),
    path('edit/<int:pk>/', PagesUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', PagesDelete.as_view(), name='delete'),
],'urlPage')

#le cambiamos el nombre de urlpatterns a cualquiera, se convierte en tupla y se asigna un nombre