from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from courses.models import Course, Lesson

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def student_list(request):
    students = Student.objects.all().order_by("pk")
    # courses = Course.objects.filter(student=pk) #TODO подумать над этим
    return render(request, 'students/student_list.html', {'stud': students})


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
            form.save_m2m()
            stud.save()
            return redirect('student_detail', pk=stud.pk)
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
            return redirect('student_detail', pk=stud.pk)
    else:
        form = StudentForm(instance=stud)
    return render(request, 'students/student_edit.html', {'form': form})


@login_required
def student_delete(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    stud.delete()
    return redirect('student_list')
