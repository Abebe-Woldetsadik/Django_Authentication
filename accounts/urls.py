from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm
from . import views

app_name = 'accounts'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/',views.register, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    
    # path('register/',views.signup.as_view(), name='signup'),
    #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), # Default login
    # reset Password urls # 
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
]
