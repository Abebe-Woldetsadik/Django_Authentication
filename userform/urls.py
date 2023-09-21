"""
URL configuration for userform project.

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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('logedin', views.Logedin.as_view(), name='logedin'),
    path('completed/', views.Completed.as_view(), name='completed'),
    path('confirm/', views.ConfirmEmail.as_view(), name='confirm'),
    path('rcompleted/', views.RegidtrationCompleted.as_view(), name='rcompleted'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls',namespace ='accounts')),
    
    # reset Password urls #
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
]
