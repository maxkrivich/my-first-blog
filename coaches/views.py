from coaches.models import Coach
from courses.models import Course, Lesson

from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect


class CoachDetailView(DetailView):
    model = Coach
    template_name = 'coaches/coach_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CoachDetailView, self).get_context_data(**kwargs)
        coach = get_object_or_404(Coach, pk=self.object.pk)
        courses = Course.objects.filter(coach=coach)
        assistant = Course.objects.filter(assistant=coach)
        context["coach"] = coach
        context["courses"] = courses
        context["assistant"] = assistant
        return context
