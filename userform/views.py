from django.views.generic import TemplateView
from django.urls import reverse_lazy

class HomePage(TemplateView):
    success_url = reverse_lazy('logedin')
    template_name = 'index.html'
class Logedin(TemplateView):
    template_name = 'home.html'

class Completed(TemplateView):
    template_name = 'accounts/activation_complete.html'
    
class ConfirmEmail(TemplateView):
    template_name = 'accounts/confirm_email.html'    
    
class RegidtrationCompleted(TemplateView):
    template_name = 'accounts/registration_completed.html'    
    