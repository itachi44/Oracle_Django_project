"""OneForAll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from one4all import views

#on importe toutes les routes depuis toutes les apps
urlpatterns = [
    url(r'^$', views.index, name='home'), #means all path like 'one4all/' c'est la page accueil 
    url(r'^result/$', views.ajax, name='ajax'),
    url(r'^mydashbord/', admin.site.urls)
]
