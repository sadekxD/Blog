from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistration(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    username = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def register(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
