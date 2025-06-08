from django.urls import path
from . import views

#Url configuration
urlpatterns = [
    path('',views.homepage, name='home'),
    path('add-college',views.addCollege,name='addCollege'),
    path('add-student',views.addStudent,name='addStudent'),
    path('student-list',views.studentList, name='student-list'),
    path('new-student',views.new_student, name='new-student')
]