from django.urls import path
from Apps.Registration.views import *

Registration_patterns = ([
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', ProfileEmailUpdate.as_view(), name='profile_email'),
],'urlRegistration') 