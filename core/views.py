from django.shortcuts import render
from study.models import *
from django.contrib.auth.models import User
from account.models import Profile

def home(request):
    # TOTALS
    total_questions = Question.objects.count()
    total_notes = NoteModel.objects.count()
    total_resources = total_questions + total_notes
    total_departments = Department.objects.count()
    total_courses = Course.objects.count()
    total_students = User.objects.count()
    
    user = request.user
    university = Profile.university
    department = Profile.department
    year = Profile.year
    semester = Profile.semester
    
    if request.user.is_authenticated:
        try:
            profile_object = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            # Handle the case where the user's profile does not exist
            pass
        
    # print('dept:', department , 'year:', year, 'sem:', semester)
    if user.is_authenticated:
        context = {
            'profile_object': profile_object,
            
            'total_resources': total_resources,
            'total_courses': total_courses,
            'total_departments': total_departments,
            'total_students': total_students,
            'university': university,
            'department_id': department,
            'year_id': year,
            'semester_id': semester,
        }
    
    else:
        context = {
            'total_resources': total_resources,
            'total_courses': total_courses,
            'total_departments': total_departments,
            'total_students': total_students,
            'university': university,
            'department_id': department,
            'year_id': year,
            'semester_id': semester,
        }

    # print(profile_object)
    return render(request, 'home.html', {'context': context})
