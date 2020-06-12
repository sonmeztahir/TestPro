from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from django.contrib.auth import authenticate

class CustomCreation(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'sinif', 'numara')

	def save(self, commit=True):
		user = super().save(commit=False)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.sinif = self.cleaned_data.get('sinif')
		user.numara = self.cleaned_data.get('numara')
		if commit:
			user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, label='Kullanıcı Adı')
	password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('Kullanıcı adını veya parolayı yanlış girdiniz!')
		return super(LoginForm, self).clean()
