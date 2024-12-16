# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Grade, Class, Student
from .forms import GradeForm, StudentForm
from django.contrib.auth.decorators import login_required

@login_required
def student_profile(request):
    student = get_object_or_404(Student, user=request.user)
    grades = student.grades.all().order_by('-date')
    average_grade = student.get_average_grade()

    classmates = student.student_class.students.exclude(id=student.id).order_by('last_name')
    
    classmates_with_grades = [(classmate, classmate.get_average_grade()) for classmate in classmates]

    return render(request, 'journal/student_profile.html', {
        'student': student,
        'grades': grades,
        'average_grade': average_grade,
        'classmates_with_grades': classmates_with_grades
    })


# @login_required
# def student_profile(request):
#     student = get_object_or_404(Student, user=request.user)
#     grades = student.grades.all().order_by('-date')
#     average_grade = student.get_average_grade()

#     classmates = student.student_class.students.exclude(id=student.id).order_by('last_name')
    
#     classmates_with_grades = [(classmate, classmate.get_average_grade()) for classmate in classmates]

#     return render(request, 'journal/student_profile.html', {
#         'student': student,
#         'grades': grades,
#         'average_grade': average_grade,
#         'classmates_with_grades': classmates_with_grades
#     })


@login_required
def journal(request):
    grades = Grade.objects.all()

    is_teacher = request.user.profile.role == 'teacher' or request.user.is_superuser
    return render(request, 'journal/journal.html', {'grades': grades, 'is_teacher': is_teacher})

# Добавление новой оценки для ученика
def add_grade(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        subject = request.POST.get('subject')
        score = request.POST.get('score')

        student = get_object_or_404(Student, id=student_id)
        Grade.objects.create(student=student, subject=subject, grade=score)
        return redirect('journal')

    students = Student.objects.all()
    return render(request, 'journal/add_grade.html', {'students': students})

# Просмотр информации об оценке
def view_grades(request, id):
    grade = get_object_or_404(Grade, id=id)
    return render(request, 'journal/view_grades.html', {'grade': grade})

@login_required
def add_student(request):
    # Проверяем, что пользователь является суперпользователем
    if not request.user.is_superuser:
        return redirect('journal')

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'journal/add_student.html', {'form': form})

# Список всех учеников
def student_list(request):
    students = Student.objects.all()
    return render(request, 'journal/student_list.html', {'students': students})

# Добавление оценки для класса
def add_class_grade(request, class_id):
    _class = get_object_or_404(Class, id=class_id)
    students = _class.students.all()

    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_grades', class_id=class_id)

    return render(request, 'journal/add_class_grades.html', {'form': form, 'students': students, 'class': _class})

# Отображение оценок класса
def class_grades(request, class_id):
    _class = get_object_or_404(Class, id=class_id)
    grades = Grade.objects.filter(student__student_class=_class)

    return render(request, 'journal/class_grades.html', {'grades': grades, 'class': _class})

