from django.shortcuts import render, redirect
from django.http import HttpResponse
from playground.forms import CollegeForm
from playground.models import Student,College

def say_hello(request):
    return render(request, 'hello.html',{'name':    'Ram'})

def say_secret(request):
    return render(request, 'secret.html')

def homepage(request):
    return render(request, 'homepage.html')

def addCollege(request):
    pass

def addStudent(request):
    pass

def studentList(request):
    students = Student.objects.select_related('college').all()
    return render(request, 'student_list.html',{'students':students})

def new_student(request):
    colleges = College.objects.all()  # Fetch all colleges

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        age = request.POST["age"]
        college_id = request.POST["college"]

        # Get the selected college object
        college = College.objects.get(id=college_id)

        # Check if a student with the same email already exists
        if Student.objects.filter(email=email).exists():
            return render(request, "newstudent.html", {
                "colleges": colleges,
                "error": "A student with this email already exists."
            })

        try:
            # Create and save the student object
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                age=age,
                college=college
            )
            return redirect("student-list")

        except IntegrityError:
            return render(request, "newstudent.html", {
                "colleges": colleges,
                "error": "An error occurred while saving the student. Please try again."
            })

    return render(request, "newstudent.html", {"colleges": colleges})

def new_college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new-college')
    else:
        form = CollegeForm()
    return render(request,'newcollege.html',{'form':form})