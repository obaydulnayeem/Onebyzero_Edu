from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # path('their_course/', views.their_course, name='their_course'),

    path('university/<int:university_id>/', views.university_detail, name='university_detail'),

    # path('my_department/<int:university_id>/<int:department_id>/<int:course_id>/', views.my_department, name='my_department'),

    path('get_access/', views.get_access, name='get_access'),

    path('sent_verification_req/', views.sent_verification_req, name='sent_verification_req'),
    
    # path('success_verification_req/', views.success_verification_req, name='success_verification_req'),
    
    path('my_department_y/<int:university_id>/<int:department_id>/', views.my_department_y, name='my_department_y'),
    
    path('my_department_s/<int:university_id>/<int:department_id>/', views.my_department_s, name='my_department_s'),
    
    path('my_university/<int:university_id>/', views.my_university, name='my_university'),
    
    path('update_department_order/', views.update_department_order, name='update_department_order'),
    
    path('scrape/', views.scrape_data, name='scrape_data'),
    
    path('pin_year_and_semester/<int:year>/<int:semester>/', views.pin_year_and_semester, name='pin_year_and_semester'),

    path('switch_department/', views.switch_department, name='switch_department'),

    path('view_course/<int:course_id>/', views.view_course, name='view_course'),
    
    path('my_resources/<int:department_id>/<int:year>/<int:semester>/', views.my_resources, name='my_resources'),
    
    path('my_resources_s/<int:department_id>/<int:semester>/', views.my_resources_s, name='my_resources_s'),

    path('my_resources_selection/', views.my_resources_selection, name='my_resources_selection'),

    # QUESTIONS---------------------------------
    path('add_question/', views.add_question, name='add_question'),

    path('view_questions/<int:course_id>/', views.view_questions, name='view_questions'),

    path('view_questions/<int:question_id>/edit/', views.edit_question, name='edit_question'),
    
    path('view_questions/<int:question_id>/delete/', views.delete_question, name='delete_question'),

    # NOTES-------------------------------------
    path('add_note/', views.add_note, name='add_note'),
    
    path('view_notes/<int:course_id>/', views.view_notes, name='view_notes'),

    # BOOKS-------------------------------------
    path('add_book/', views.add_book, name='add_book'),
    
    path('view_books/<int:course_id>/', views.view_books, name='view_books'),
    
    # LECTURE SLIDES -------------------------------------
    path('add_lecture/', views.add_lecture, name='add_lecture'),
    
    path('view_lectures/<int:course_id>/', views.view_lectures, name='view_lectures'),
    
    # FEEDBACKS ============================================
    path('submit-feedback/<int:question_id>/', views.submit_feedback, name='submit_feedback'),
   
    path('success-feedback/', views.success_feedback, name='success_feedback'),
    
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    
    
    # path('handle_love_click/<int:question_id>/', views.handle_love_click, name='handle_love_click'),
    
    # path('update_love_count/', views.increment_love_count, name='increment_love_count'),
    
    path('share/<int:question_id>/', views.share_question, name='share_question'),

    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'), # AJAX

    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX

    path('ajax/load-teachers/', views.load_teachers, name='ajax_load_teachers'), # AJAX
    
    # path('department_list/', views.nothing, name='nothing'),

    path('need_verification/', views.need_verification, name='need_verification'),

    path('leaderboard/', views.leaderboard, name='leaderboard'),

    # TEST PURPOSE ===============================================
    path('nothing/', views.nothing, name='nothing'),

    path('test_page1/', views.test_page1, name='test_page1'),

    path('test_page2/', views.test_page2, name='test_page2'),

    path('make_user_ambassador/<int:department_id>/', views.make_user_ambassador, name='make_user_ambassador'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
