from django.contrib import admin
from .models import Student, Class, Grade, Subject

# Регистрация моделей в административной панели Django
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Grade)
admin.site.register(Subject)