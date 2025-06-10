from django import forms

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name', 'address', 'established_year']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'enrollment_date', 'college']

