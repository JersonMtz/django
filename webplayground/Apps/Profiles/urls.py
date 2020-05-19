from django.urls import path
from Apps.Profiles.views import ProfilesListView, ProfilesDetailView

Profiles_patterns = ([
    path('', ProfilesListView.as_view(), name='list'),
    path('<username>/', ProfilesDetailView.as_view(), name='detail'),
],'urlProfiles')

#le cambiamos el nombre de urlpatterns a cualquiera, se convierte en tupla y se asigna un nombre