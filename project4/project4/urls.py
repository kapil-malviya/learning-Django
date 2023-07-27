"""
URL configuration for project4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
#from greetingapp.views import greetings_view
#from timeapp.views import time_info_view
from greetingapp import views as v8
from timeapp import views as v88

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('greeting/', greetings_view),
#    path('time/', time_info_view)
    path('greeting/', v8.greetings_view),
    path('time/', v88.time_info_view)
]
