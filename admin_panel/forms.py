from django import forms
from study.models import Course

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'credit', 'hour', 'syllabus']
        
        labels = {
            'title': 'Course Title',
            'code': 'Course Code',
            'credit': 'Credit Hours',
            'hour': 'Weekly Hours',
            'syllabus': 'Syllabus',
        }
    
        placeholders = {
            'title': 'Enter course title...',
            'code': 'Enter course code...',
            'credit': 'Enter credit hours...',
            'hour': 'Enter weekly hours...',
            'syllabus': 'Enter course syllabus...',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control'}),
            'hour': forms.NumberInput(attrs={'class': 'form-control'}),
            'syllabus': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        # error_messages = {
        #     'title': {'required': 'Please enter the course title.'},
        #     'code': {'required': 'Please enter the course code.'},
        #     'credit': {'required': 'Please enter the credit hours.'},
        #     'hour': {'required': 'Please enter the weekly hours.'},
        #     'syllabus': {'required': 'Please enter the course syllabus.'},
        # }
        
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'