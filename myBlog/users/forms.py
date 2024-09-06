from django import forms    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='username')
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label='username')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

