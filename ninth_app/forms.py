# forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class Name(forms.Form):
	name = forms.CharField(max_length = 30)

class Email(forms.Form):
	email = forms.EmailField()

class Age(forms.Form):
	age = forms.IntegerField()