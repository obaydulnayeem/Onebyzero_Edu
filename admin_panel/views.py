# admin_panel/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import PendingUserModel, Profile
from study.models import Course
from django.contrib.auth.models import User
from .forms import EditCourseForm, AddCourseForm
from django.contrib import messages

@login_required
def admin_dashboard(request):
    admin_id = request.user.id
    admin_info = Profile.objects.get(user_id=admin_id)
    
    context = {
        'admin_info': admin_info,
    }
    return render(request, 'admin_dashboard.html', context)

def pending_for_verify_users(request):
    pending_users = PendingUserModel.objects.all()
    return render(request, 'batch_ambassadors/pending_for_verify_users.html', {'pending_users': pending_users})

def batch_wise_users(request):
    batch_wise_users = Profile.objects.all()
    return render(request, 'batch_ambassadors/batch_wise_users.html', {'batch_wise_users': batch_wise_users})

def make_verified_user(request, user_id):
    if request.method == 'POST':
        # user_id = request.POST.get('user_id')
        # print('useriddd', user_id)
        # user = User.objects.get(id=user_id)
        # user.is_verified = True
        user = get_object_or_404(Profile, id=user_id)
        print(user)
        user.is_verified = True
        user.save()
        return redirect('pending_for_verify_users')
    return render(request, 'admin_dashboard.html')

def make_not_verified_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(Profile, id=user_id)
        user.is_verified = False
        user.save()
        return redirect('batch_wise_users')
    return render(request, 'admin_dashboard.html')

def view_courses(request, university_id, department_id, year_id, semester_id):
    courses = Course.objects.filter(university_id=university_id, department_id=department_id, year=year_id, semester=semester_id)
    
    # print(university_id, department_id, year_id, sem_id)
    
    return render(request, 'batch_ambassadors/view_courses.html', {'courses': courses})



def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    
    university_id = course.university.id
    department_id = course.department.id
    year_id = course.year
    semester_id = course.semester
    
    # print(sem_id)
    
    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=course)
        print(form.errors)
        if form.is_valid():
            form.save()
            # messages(success='Course updated successfully!')
            messages.success(request, "Course updated successfully!")
            return redirect('view_courses', university_id=university_id, department_id=department_id, year_id=year_id, semester_id=semester_id)
    else:
        form = EditCourseForm(instance=course)
    return render(request, 'batch_ambassadors/edit_course.html', {'form': form, 'course': course})

def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        university_id = request.POST.get('university')
        department_id = request.POST.get('department')
        year_id = request.POST.get('year')
        semester_id = request.POST.get('semester')
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('view_courses', university_id=university_id, department_id=department_id, year_id=year_id, semester_id=semester_id)
    else:
        form = AddCourseForm()
    return render(request, 'batch_ambassadors/add_course.html', {'form': form})