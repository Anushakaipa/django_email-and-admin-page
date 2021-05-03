from django import forms
from django.contrib.auth.forms import UserCreationForm
from Med.models import User


class UsrReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
	class Meta:
		model = User 
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"username",
			}),
		}

class UsPerm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','email','role']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"username","readOnly":True}),
		"email":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"email","readOnly":True}),
		"role":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"role",}),
		}
