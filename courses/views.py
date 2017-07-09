from django.utils import timezone
from courses.models import Course, Lesson
from .forms import CourseForm, LessonForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': Course.objects.get(pk=pk),
                                                          'lesson': Lesson.objects.filter(course=pk).order_by("order"), })


@login_required
def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'courses/course_edit.html', {'form': form})


@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('/')


@login_required
def add_lesson_to_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            less = form.save(commit=False)
            less.course = course
            less.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = LessonForm()
    return render(request, 'courses/add_lesson_to_course.html', {'form': form})


@login_required
def lesson_new(request):
    pass


@login_required
def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            less = form.save(commit=False)
            less.save()
            return redirect('course_detail', pk=lesson.course.pk)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'courses/add_lesson_to_course.html', {'form': form})


@login_required
def lesson_delete(request, pk):
    less = get_object_or_404(Lesson, pk=pk)
    course_id = less.course.pk
    less.delete()
    return redirect('course_detail', pk=course_id)
