from django.forms import ModelForm
from django import forms
from .models import File


class FileForm(forms.ModelForm):
	class Meta:
		model= File
		fields= ["name","author","upload_file","Specialized","General"]


class RegisterForm(forms.Form):
	first_name= forms.CharField(label= 'First Name')
	last_name= forms.CharField(label= 'Last Name')
	password= forms.CharField(label= 'Password', widget= forms.PasswordInput)
	confirm_password= forms.CharField(label= 'Confirm Password', widget= forms.PasswordInput)
	email= forms.EmailField(label= 'Email')
	def clean(self):
		cleaned_data= super().clean()
		password= cleaned_data.get('password')
		confirm_password= cleaned_data.get('confirm_password')
		if password and confirm_password and password != confirm_password:
			raise forms.ValidationError("Password and confirmed password doesn't match.")






	
