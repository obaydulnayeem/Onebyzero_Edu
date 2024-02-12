from django.db import models
from .choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from account.models import Profile
from django.conf import settings

SYSTEM_CHOICES = (
    ('year', 'Year'),
    ('semester', 'Semester'),
)

# SEMESTER_CHOICES = (
#     (FIRST_SEM, '1st'),
#     (SECOND_SEM, '2nd'),
#     (THIRD_SEM, '3rd'),
#     (FOURTH_SEM, '4th'),
#     (FIFTH_SEM, '5th'),
#     (SIXTH_SEM, '6th'),
#     (SEVENTH_SEM, '7th'),
#     (EIGHTH_SEM, '8th'),
# )

# YEAR_CHOICES = (
#     (FIRST_YEAR, '1st'),
#     (SECOND_YEAR, '2nd'),
#     (THIRD_YEAR, '3rd'),
#     (FOURTH_YEAR, '4th'),
# )

class University(models.Model):
    name = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    # established = models.DateField()
    # university_type = models.CharField(max_length=100, choices=UNIVERSITY_TYPE_CHOICES)
    def __str__(self):
        return f'{self.name}'

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

class Department(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    system = models.CharField(max_length=100, choices=SYSTEM_CHOICES, default='semester')
    established = models.DateField(blank = True, null = True)
    num_of_seat = models.PositiveIntegerField(default=0)
    ambassadors = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    def __str__(self):
        return f'{self.name}'

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default = 1)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default = 1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default = 1)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    hour = models.PositiveIntegerField(default=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES, blank=True, null=True)
    syllabus = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

class Question(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50, choices=EXAM_CHOICES)
    session = models.CharField(max_length=9, choices=SESSION_CHOICES)
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default = 1)
    question_file = models.FileField(upload_to='study/questions/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.exam_name
    
class NoteModel(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # exam_name = models.CharField(max_length=50, choices=EXAM_CHOICES)
    session = models.CharField(choices=SESSION_CHOICES, max_length=50)
    note_title = models.CharField(max_length=200)
    note_author = models.CharField(max_length=100)
    note_file = models.FileField(upload_to='study/notes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.note_title
    
class BookModel(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # session = models.CharField(choices=SESSION_CHOICES, max_length=50)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_file = models.FileField(upload_to='study/books/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.book_title    


class LectureModel(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.CharField(choices=SESSION_CHOICES, max_length=50)
    lecture_title = models.CharField(max_length=200)
    lecture_author = models.CharField(max_length=100)
    lecture_file = models.FileField(upload_to='study/lectures/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.lecture_title
