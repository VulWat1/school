from django.urls import path
from . import views
from journal import views as journal_views

urlpatterns = [
    path("", views.main, name='home'),
    path("about", views.about, name='about'),
    path('journal/', journal_views.student_profile, name='student_profile'),
    path('features', views.features, name='features')
]
