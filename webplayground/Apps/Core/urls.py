from django.urls import path
from Apps.Core.views import *

urlpatterns = [
    path('', PageIndexView.as_view(), name="home"),
    path('sample/', PageSampleView.as_view(), name="sample"),
]