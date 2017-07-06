from django.utils import timezone
from .models import Course, Lesson


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
