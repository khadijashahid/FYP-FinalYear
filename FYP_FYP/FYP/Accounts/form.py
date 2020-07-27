from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


class CreateUserForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']