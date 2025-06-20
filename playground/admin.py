from django.contrib import admin

from playground.models import College
from playground.models import Student

# Register your models here.
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'established_year')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age', 'enrollment_date', 'college')
