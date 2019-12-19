"""mysite URL Configuration

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
from django.urls import path, include


urlpatterns = [
 path('polls/', include('polls.urls')), # import에 include 적어야됨
    #path('polls1/', include('polls1.urls')), 앱을 추가 시켜 연결가능
    #path('polls2/', include('polls2.urls')),
    #path('polls3/', include('polls3.urls')),
 path('admin/', admin.site.urls),
]
