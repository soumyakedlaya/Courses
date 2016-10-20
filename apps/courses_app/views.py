from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
    "courses": Course.objects.all() #run a select * from Course
    }
    return render(request, "courses_app/index.html", context)

def add_course(request):
    Course.objects.create(name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')

def delete(request, id):
    context = {
        "selectedcourse": Course.objects.get(id=id)
    }
    return render(request, "courses_app/confirmdel.html", context)

def confirm_delete(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')
