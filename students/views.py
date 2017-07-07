from django.shortcuts import render
from .models import Student
from courses.models import Course, Lesson

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def student_list(request):
    students = Student.objects.all().order_by("pk")
    return render(request, 'students/student_list.html', {'stud': students})


def student_detail(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    courses = Course.objects.filter(student=pk)
    print(courses)
    return render(request, 'students/student_detail.html', {'stud': stud, 'course':courses})
