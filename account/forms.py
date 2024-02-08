from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from study.models import University, Department


# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from study.models import University, Department
from .models import User, Profile
from study.choices import SESSION_CHOICES, DEPARTMENTAL_BATCHES

class SignupForm(UserCreationForm):
    fullname = forms.CharField(max_length=100, required=True)
    nickname = forms.CharField(max_length=100, required=False)
    university = forms.ModelChoiceField(queryset=University.objects.all(), required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)
    session = forms.ChoiceField(choices=SESSION_CHOICES, required=True)
    departmental_batch = forms.ChoiceField(choices=DEPARTMENTAL_BATCHES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include other fields from the User model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['university'].label = 'University'
        self.fields['department'].label = 'Department'

        if all(field in self.data for field in ['university', 'department']):
            try:
                university_id = int(self.data.get('university'))
                department_id = int(self.data.get('department'))
                
                # Filter the 'department' queryset based on the selected 'university'.
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')

            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['department'].queryset = self.instance.university.department_set.order_by('name')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        # Create a Profile instance and associate it with the user
        profile = Profile.objects.create(user=user,
        email = self.cleaned_data['email'], 
        fullname = self.cleaned_data['fullname'], 
        nickname = self.cleaned_data['nickname'],
        university=self.cleaned_data['university'], department=self.cleaned_data['department'],
        session=self.cleaned_data['session'],
        departmental_batch=self.cleaned_data['departmental_batch'])

        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'user_type', 'profile_image', 'email', 'university', 'department', 'session', 'departmental_batch', 'year', 'semester']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ['bio', 'fullname', 'nickname', 'profile_image', 'email', 'university', 'department', 'session', 'departmental_batch', 'year', 'semester', 'facebook_id', 'codeforces_id']
        exclude = ['last_updated']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.none()
        self.fields['departmental_batch'].required = False
        
        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance and self.instance.university: 
            self.fields['department'].queryset = self.instance.university.department_set.order_by('name')

