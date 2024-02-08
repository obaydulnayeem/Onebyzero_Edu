# admin_panel/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    
    path('batch_wise_users/', batch_wise_users, name='batch_wise_users'),
    
    path('pending_for_verify_users/', pending_for_verify_users, name='pending_for_verify_users'),
    
    path('make_verified_user/<int:user_id>/', make_verified_user, name='make_verified_user'),
    
    path('make_not_verified_user/<int:user_id>/', make_not_verified_user, name='make_not_verified_user'),
    
    
    path('view_courses/<int:university_id>/<int:department_id>/<int:year_id>/<int:semester_id>/', view_courses, name='view_courses'),
    
    path('edit_course/<int:course_id>/', edit_course, name='edit_course'),
    
    path('add_course/', add_course, name='add_course'),
]
