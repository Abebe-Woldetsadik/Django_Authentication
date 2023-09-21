from django import forms
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

User = get_user_model()
class UsersCreationForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name' ,'last_name' ,'password1', 'password2' )
        
        
        def __init__(self,*args, **kwargs):
            super.__init__(*args, **kwargs)
            self.fields['username'].lable = 'Display Name'
            self.fields['Email'].lable = 'Email Address'
            
        def clean_email(self):
            """Validate the uniqueness of the email field."""
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already in use.")
            return email
            
            # user_count = get_user_model.objects.filter(email=email.count())
            # if user_count > 1:
            #     raise forms.ValidationError("This Email has already been registered. please check and try again or reset your password")
            # return email  
        
class UserLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())



# class FormWithCaptcha(forms.Form):
#     captcha = ReCaptchaField()
