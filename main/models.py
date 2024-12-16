from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')
    
    class Meta:
        permissions = [
            ('can_add_grades', 'Can add grades'),
            ('can_view_all_students', 'Can view all students'),
        ]


    def __str__(self):
        return f"{self.username} - {self.role}"
