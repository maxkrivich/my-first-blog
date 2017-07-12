from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from courses.models import Course, Lesson
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

handler = logging.FileHandler(os.path.join("./", "students_logger.log"), "w", encoding=None, delay="true")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    template_name = 'students/student_list.html'


    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id is not None:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id')
        if course_id is not None:
            course = get_object_or_404(Course, pk=course_id)
            pagination_prefix = '?course_id={}&'.format(course_id)
            context['title'] = 'Students on {}:'.format(course.name)
        else:
            pagination_prefix = '?'
            context['title'] ='List of students:'
        context['pagination_prefix'] = pagination_prefix
        return context


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


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

    def get_context_data(self, **kwargs):
        logger.debug('Students detail view has been debugged!')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context["stud"] = get_object_or_404(Student, pk=self.object.pk)
        return context


def student_detail(request, pk):
    stud = get_object_or_404(Student, pk=pk)
    # courses = Course.objects.filter(student=pk)
    # # print(courses)
    return render(request, 'students/student_detail.html', {'stud': stud})


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/student_edit.html'
    form_class = StudentForm
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, 'Student {} successfully added'.format(
            self.object.full_name()))
        return form


@login_required
def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            stud = form.save(commit=False)
            form.save()
            stud.save()
            messages.success(
                request, 'Student {} successfully added'.format(stud.full_name()))
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_edit.html', {'form': form})


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/student_edit.html'
    form_class = StudentForm
    success_url = '#'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, 'Information successfully changed')
        return form


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


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_delete.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context["stud"] = self.object
        return context

    def delete(self, request, *args, **kwargs):
        res = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Student {} successfully removed'.format(
            self.object.full_name()))
        return res


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
