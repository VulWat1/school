# school/journal/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.journal, name='journal'),
    path('login/', LoginView.as_view(template_name='journal/login.html'), name='login'),
    path('profile/', views.student_profile, name='student_profile'),
    path('grades/', views.view_grades, name='view_grades'),
    path('add/', views.add_grade, name='add_grade'),
    path('add_student/', views.add_student, name='add_student'),
    path('students/', views.student_list, name='student_list'),
    path('grades/<int:class_id>/', views.class_grades, name='class_grades'),
    path('add_grade/<int:class_id>/', views.add_grade, name='add_class_grades'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
]
