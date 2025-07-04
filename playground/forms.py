from django import forms
from playground.models import College
from playground.models import Student

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name', 'address', 'established_year']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'college']

