from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomCreation(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'sinif', 'numara')

	def save(self, commit=True):
		user = super().save(commit=False)
		user.sinif = self.cleaned_data.get('sinif')
		user.numara = self.cleaned_data.get('numara')
		if commit:
			user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, label='Kullanıcı Adı')
	password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)


