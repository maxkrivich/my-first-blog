import re
from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from courses.models import Course, Lesson
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect


def student_list(request):
    if 'course_id' in request.GET:
        course = get_object_or_404(Course, pk=request.GET.get('course_id'))
        students = Student.objects.filter(courses=course.pk)
        title = 'Students on {}:'.format(course.name)
    else:
        title = 'List of students:'
        students = Student.objects.all().order_by("pk")
    paginator = Paginator(students, 2)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, 'students/student_list.html', {'stud': students, 'title': title})


def students_on_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    stud = Student.objects.filter(courses=course.pk)
    return render(request, 'students/student_list.html', {'stud': stud, 'title': 'test'})


def student_detail(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    # courses = Course.objects.filter(student=pk)
    # # print(courses)
    return render(request, 'students/student_detail.html', {'stud': stud})


@login_required
def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            stud = form.save(commit=False)
            form.save()
            stud.save()
            messages.success(
                request, 'Student {} successfully added'.format(stud.full_name))
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_edit.html', {'form': form})


@login_required
def student_edit(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=stud)
        if form.is_valid():
            stud = form.save(commit=False)
            form.save_m2m()
            stud.save()
            messages.success(request, 'Information successfully changed')
            return redirect('student_edit', pk=stud.pk)
    else:
        form = StudentForm(instance=stud)
    return render(request, 'students/student_edit.html', {'form': form})


@login_required
def student_delete(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        messages.success(
            request, 'Student {} successfully removed'.format(stud.full_name()))
        stud.delete()
        return redirect('student_list')
    else:
        return render(request, 'students/student_delete.html', {'stud': stud})
