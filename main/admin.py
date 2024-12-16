from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'get_role', 'is_staff', 'is_superuser']
    list_filter = ['is_teacher', 'is_student', 'is_parent', 'is_staff']
    search_fields = ['username', 'email']

    def get_role(self, obj):
        if obj.is_teacher:
            return "Teacher"
        elif obj.is_student:
            return "Student"
        elif obj.is_parent:
            return "Parent"
        return "Unknown"

    get_role.short_description = 'Role'
