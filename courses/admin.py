from django.contrib import admin
from .models import Course, Lesson

class LessonInline(admin.TabularInline):
	model = Lesson
	extra = 3

admin.site.register(Lesson)

class CourseAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ('name', 'short_description')
	inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
