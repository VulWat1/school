from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Классы школы (например, 2-А, 5-Б)
class Class(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Ученик

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Исправлено
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.ForeignKey('Class', on_delete=models.CASCADE)
    grades = models.ManyToManyField('Grade', related_name='student_grades')

    def __str__(self):
        return f"{self.user.username}"

# Учитель
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

# Администратор (дополнительно можно использовать Groups и Permissions)
class Administrator(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

# Предметы школы
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Оценки для учеников
class Grade(models.Model):
    student = models.ForeignKey('journal.Student', on_delete=models.CASCADE, related_name='grades_received')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    grade = models.PositiveSmallIntegerField()
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"

# Профиль пользователя
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"

