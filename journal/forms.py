# forms.py
from django import forms
from .models import Grade, Student, Class

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_class']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # Динамически заполняем поле student_class
        self.fields['student_class'].queryset = Class.objects.all()
