from django.utils import timezone
from courses.models import Course, Lesson
from .forms import CourseForm, LessonForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

import os.path
import logging

log_format = '%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

handler = logging.FileHandler(os.path.join("./", "courses_logger.log"), "w", encoding=None, delay="true")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)



class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, **kwargs):
        logger.debug('Courses detail view has been debugged!')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, pk=self.object.pk)
        context["course"] = Course.objects.get(pk=self.object.pk)
        context["lesson"] = Lesson.objects.filter(
            course=self.object.pk).order_by("order")
        return context


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Course.objects.all()


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        return context

    def delete(self, request, *args, **kwargs):
        res = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(
            request, 'Course {} successfully removed'.format(self.object.name))
        return res


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/course_edit.html'
    form_class = CourseForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form = super(CourseCreateView, self).form_valid(form)
        messages.success(self.request, 'Course {} successfully created'.format(
            self.object.name))
        return form


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/course_edit.html'
    form_class = CourseForm
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form = super(CourseUpdateView, self).form_valid(form)
        messages.success(self.request, 'Course information {} successfully updated'.format(
            self.object.name))
        return form


class LessonUpdateView(UpdateView):
    model = Lesson
    template_name = 'courses/add_lesson_to_course.html'
    form_class = LessonForm

    def get_success_url(self):
        course = self.object.course
        return reverse_lazy('course_detail', kwargs={'pk': course.id})

    def get_context_data(self, **kwargs):
        context = super(LessonUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form = super(LessonUpdateView, self).form_valid(form)
        messages.success(self.request, 'Lesson information {} successfully updated'.format(
            self.object.subject))
        return form


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'courses/lesson_delete.html'

    def get_success_url(self):
        course = self.object.course
        return reverse_lazy('course_detail', kwargs={'pk': course.id})

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)
        context["lesson"] = self.object
        return context

    def delete(self, request, *args, **kwargs):
        res = super(LessonDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Lesson {} successfully removed'.format(
            self.object.subject))
        return res


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'courses/add_lesson_to_course.html'

    def get_success_url(self):
        course = self.object.course
        return reverse_lazy('course_detail', kwargs={'pk': course.id})

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form = super(LessonCreateView, self).form_valid(form)
        messages.success(self.request, 'Lesson information {} successfully updated'.format(
            self.object.subject))
        return form


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
