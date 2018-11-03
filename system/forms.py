from allauth.account.forms import LoginForm
from django import forms


class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'login'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'password'})