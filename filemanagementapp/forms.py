from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password = forms.CharField(min_length=6, max_length=32)
    repeat_password = forms.CharField(min_length=6, max_length=32)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("This email is already in use")
        except User.DoesNotExist:
            return email

    def clean(self):
        super(RegisterForm, self).clean()
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('repeat_password')
        if not password == re_password:
            raise forms.ValidationError('Passwords must match')

    def create(self, validated_data):
        # create a auth user
        user = User.objects.create_user(
            username=validated_data['email'], email=validated_data['email'], password=validated_data['password']
        )
        return user


