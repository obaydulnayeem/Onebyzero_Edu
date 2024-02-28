from django import forms
from .models import *
from account.models import Profile
from django.contrib.auth.models import User

class UniversityForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all(), empty_label="Select a university")

class DepartmentForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select a department")

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
 
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['university', 'department', 'semester', 'course', 'exam_name', 'session', 'question_file']
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         self.fields['department'].queryset = Department.objects.none()
#         self.fields['course'].queryset = Course.objects.none()
#         # self.fields['course_teacher'].queryset = Teacher.objects.all()

#         if all(field in self.data for field in ['university', 'department', 'semester']):
#             try:
#                 university_id = int(self.data.get('university'))
#                 department_id = int(self.data.get('department'))
#                 # year = int(self.data.get('year'))
#                 semester = int(self.data.get('semester'))
                
#                 # Filter the 'department' queryset based on the selected 'university'.
#                 self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
                
#                 # Filter the 'course' queryset based on 'university', 'department', 'year', and 'semester'.
#                 # self.fields['course'].queryset = Course.objects.filter(department_id=department_id, year=year, semester=semester).order_by('title')
                
#                 # self.fields['course_teacher'].queryset = Teacher.objects.filter(university_id=university_id, department_id=department_id).order_by('name')

#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk:
#             # If the form is for an instance (editing an existing instance), set the queryset based on the instance's data.
#             # You'll need to replace these with the appropriate logic based on your model structure.
            
#             self.fields['department'].queryset = self.instance.university.department_set.order_by('name')
            
#             self.fields['course'].queryset = self.instance.department.course_set.filter(semester=self.instance.semester).order_by('title')
            
#             # self.fields['course_teacher'].queryset = self.instance.university.teacher_set.filter(department=self.instance.department).order_by('name')
            
#             # self.fields['course_teacher'].queryset = Teacher.objects.filter(university_id=self.instance.university_id, department_id=self.instance.department_id).order_by('name')

#             # Set the initial value for the 'course_teacher' field to the instance's course_teacher
#             # self.initial['course_teacher'] = self.instance.course_teacher


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['university', 'department', 'semester', 'course', 'exam_name', 'session', 'question_file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
                if 'department' in self.data:
                    department_id = int(self.data.get('department'))
                    semester = int(self.data.get('semester')) if 'semester' in self.data else None
                    self.fields['course'].queryset = Course.objects.filter(department_id=department_id, semester=semester).order_by('title')
            except (ValueError, TypeError):
                pass  # Invalid input - leave queryset empty or set to a default


class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['university', 'department', 'semester', 'course', 'session', 'note_title', 'note_author', 'note_file']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
                if 'department' in self.data:
                    department_id = int(self.data.get('department'))
                    semester = int(self.data.get('semester')) if 'semester' in self.data else None
                    self.fields['course'].queryset = Course.objects.filter(department_id=department_id, semester=semester).order_by('title')
            except (ValueError, TypeError):
                pass  # Invalid input - leave queryset empty or set to a default
        
class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['university', 'department', 'semester', 'course', 'book_title', 'book_author', 'book_file']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
                if 'department' in self.data:
                    department_id = int(self.data.get('department'))
                    semester = int(self.data.get('semester')) if 'semester' in self.data else None
                    self.fields['course'].queryset = Course.objects.filter(department_id=department_id, semester=semester).order_by('title')
            except (ValueError, TypeError):
                pass  # Invalid input - leave queryset empty or set to a default
        
class LectureForm(forms.ModelForm):
    class Meta:
        model = LectureModel
        fields = ['university', 'department', 'semester', 'course', 'session',  'lecture_title', 'lecture_author', 'lecture_file']
    
class MyDepartmentForm(forms.Form):
    university = forms.ModelChoiceField(
        queryset=University.objects.all(),
        empty_label="Select a university",
        widget=forms.Select(attrs={'id': 'id_university'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select a department",
        widget=forms.Select(attrs={'id': 'id_department'})
    )

class SwitchDepartmentForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['university', 'department']
    
class MyResourcesSelectionForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.none())
    semester = forms.IntegerField()
    year = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.none()

        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input from the client; ignore and fallback to an empty queryset
            
class MakeAmbassadorForm(forms.Form):
    selected_users = forms.ModelMultipleChoiceField(
        queryset=Profile.objects.all(),  # Replace with your user profile queryset
        widget=forms.CheckboxSelectMultiple,
    )
    
    def __init__(self, *args, **kwargs):
        department_id = kwargs.pop('department_id', None)
        super(MakeAmbassadorForm, self).__init__(*args, **kwargs)

        # Define 'department_id' as a hidden field
        self.fields['department_id'] = forms.IntegerField(widget=forms.HiddenInput(), initial=department_id)