from django.contrib import admin
from .models import Student

class StudenAdmin(admin.ModelAdmin):
	search_fields = ['surname', 'email',]
	list_display = ('name', 'email', 'skype',)
	list_filter = ('courses',)
	filter_horizontal = ('courses',)
	fieldsets = [
		('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
		('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
		(None, {'fields': ['courses']})
	]


admin.site.register(Student, StudenAdmin)
