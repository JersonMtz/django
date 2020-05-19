"""webplayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from Apps.Registration.urls import Registration_patterns
from Apps.Page.urls import Page_patterns
from Apps.Profiles.urls import Profiles_patterns
from Apps.Messenger.urls import Messenger_patterns

urlpatterns = [
    path('', include('Apps.Core.urls')),
    path('pages/', include(Page_patterns)),
    path('admin/', admin.site.urls),
    #URLS AUTH
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include(Registration_patterns)),
    #URL PROFILES
    path('profiles/', include(Profiles_patterns)),
    #URL Messenger
    path('messenger/', include(Messenger_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)