from django.contrib import admin
from .models import Coach
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class StaffFilter(admin.SimpleListFilter):
    title = 'staff status'
    parameter_name = 'is_staff'
    default_value = None

    # Set the displaying options
    def lookups(self, request, model_admin):
        return (
            ('YES', ('Yes')),
            ('NO', ('No')),
        )

    # Assign a query for each option
    def queryset(self, request, queryset):
        if self.value() in ('YES', 'Yes', 'yes'):
            # print(User.objects.filter(is_staff=True))
            return queryset.filter(user__in=User.objects.filter(is_staff=True))
        elif self.value() in ('NO', 'No', 'no'):
            # print(User.objects.filter(is_staff=False))
            return queryset.filter(user__in=User.objects.filter(is_staff=False))


class CoachAdmin(admin.ModelAdmin):
    model = Coach
    list_display = ('first_name', 'last_name',
                    'gender', 'skype', 'description')
    list_filter = (StaffFilter, )


admin.site.register(Coach, CoachAdmin)
