from study.models import Department
from study.models import *
from django.db.models import Sum

def department_s_context_view(request):
    # user = request.user.id
    department_id = None

    # Assuming department_id is passed in the URL, for example: /department/1/
    if 'department_id' in request.resolver_match.kwargs:
        department_id = request.resolver_match.kwargs['department_id']


    # TOTAL COURSES - SEMESTER WISE==========================
    courses_sem1 = Course.objects.filter(department = department_id, semester=1).count()
    
    courses_sem2 = Course.objects.filter(department = department_id, semester=2).count()
    
    courses_sem3 = Course.objects.filter(department = department_id, semester=3).count()
    
    courses_sem4 = Course.objects.filter(department = department_id, semester=4).count()
    
    courses_sem5 = Course.objects.filter(department = department_id, semester=5).count()
    
    courses_sem6 = Course.objects.filter(department = department_id, semester=6).count()
    
    courses_sem7 = Course.objects.filter(department = department_id, semester=7).count()
    
    courses_sem8 = Course.objects.filter(department = department_id, semester=8).count()
    
    total_courses_s = Course.objects.filter(department = department_id).count()
    
    # TOTAL CREDITS SEMESTER WISE===============================
    credits_sem1 = Course.objects.filter(department = department_id, semester=1).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem2 = Course.objects.filter(department = department_id, semester=2).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem3 = Course.objects.filter(department = department_id, semester=3).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem4 = Course.objects.filter(department = department_id, semester=4).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem5 = Course.objects.filter(department = department_id, semester=5).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem6 = Course.objects.filter(department = department_id, semester=6).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem7 = Course.objects.filter(department = department_id, semester=7).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem8 = Course.objects.filter(department = department_id, semester=8).aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0

    total_credits_s = credits_sem1 + credits_sem2 + credits_sem3 + credits_sem4 + credits_sem5 + credits_sem6 + credits_sem7 + credits_sem8
   
   
    # TOTAL HOURS SEMESTER WISE===============================
    hours_sem1 = Course.objects.filter(department = department_id, semester=1).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem2 = Course.objects.filter(department = department_id, semester=2).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem3 = Course.objects.filter(department = department_id, semester=3).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem4 = Course.objects.filter(department = department_id, semester=4).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem5 = Course.objects.filter(department = department_id, semester=5).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem6 = Course.objects.filter(department = department_id, semester=6).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem7 = Course.objects.filter(department = department_id, semester=7).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem8 = Course.objects.filter(department = department_id, semester=8).aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    total_hours_s = hours_sem1 + hours_sem2 + hours_sem3 + hours_sem4 + hours_sem5 + hours_sem6 + hours_sem7 + hours_sem8
    
    # TOTAL RESOURCES SEMESTER WISE===============================
    total_resources_sem1 = Question.objects.filter(department = department_id, semester=1).count() + BookModel.objects.filter(department = department_id, semester=1).count() + LectureModel.objects.filter(department = department_id, semester=1).count() + NoteModel.objects.filter(department = department_id, semester=1).count()
    
    total_resources_sem2 = Question.objects.filter(department = department_id, semester=2).count() + BookModel.objects.filter(department = department_id, semester=2).count() + LectureModel.objects.filter(department = department_id, semester=2).count() + NoteModel.objects.filter(department = department_id, semester=2).count()
    
    total_resources_sem3 = Question.objects.filter(department = department_id, semester=3).count() + BookModel.objects.filter(department = department_id, semester=3).count() + LectureModel.objects.filter(department = department_id, semester=3).count() + NoteModel.objects.filter(department = department_id, semester=3).count()
    
    total_resources_sem4 = Question.objects.filter(department = department_id, semester=4).count() + BookModel.objects.filter(department = department_id, semester=4).count() + LectureModel.objects.filter(department = department_id, semester=4).count() + NoteModel.objects.filter(department = department_id, semester=4).count()
    
    total_resources_sem5 = Question.objects.filter(department = department_id, semester=5).count() + BookModel.objects.filter(department = department_id, semester=5).count() + LectureModel.objects.filter(department = department_id, semester=5).count() + NoteModel.objects.filter(department = department_id, semester=5).count()
    
    total_resources_sem6 = Question.objects.filter(department = department_id, semester=6).count() + BookModel.objects.filter(department = department_id, semester=6).count() + LectureModel.objects.filter(department = department_id, semester=6).count() + NoteModel.objects.filter(department = department_id, semester=6).count()
    
    total_resources_sem7 = Question.objects.filter(department = department_id, semester=7).count() + BookModel.objects.filter(department = department_id, semester=7).count() + LectureModel.objects.filter(department = department_id, semester=7).count() + NoteModel.objects.filter(department = department_id, semester=7).count()
    
    total_resources_sem8 = Question.objects.filter(department = department_id, semester=8).count() + BookModel.objects.filter(department = department_id, semester=8).count() + LectureModel.objects.filter(department = department_id, semester=8).count() + NoteModel.objects.filter(department = department_id, semester=8).count()
    
    total_resources_all_sem = total_resources_sem1 + total_resources_sem2 + total_resources_sem3 + total_resources_sem4 + total_resources_sem5 + total_resources_sem6 + total_resources_sem7 + total_resources_sem8
    
    context = {
        'total_courses_s': total_courses_s,

        'courses_sem1': courses_sem1,
        'courses_sem2': courses_sem2,
        'courses_sem3': courses_sem3,
        'courses_sem4': courses_sem4,
        'courses_sem5': courses_sem5,
        'courses_sem6': courses_sem6,
        'courses_sem7': courses_sem7,
        'courses_sem8': courses_sem8,
        
        'credits_sem1': credits_sem1,
        'credits_sem2': credits_sem2,
        'credits_sem3': credits_sem3,
        'credits_sem4': credits_sem4,
        'credits_sem5': credits_sem5,
        'credits_sem6': credits_sem6,
        'credits_sem7': credits_sem7,
        'credits_sem8': credits_sem8,
        
        'hours_sem1': hours_sem1,
        'hours_sem2': hours_sem2,
        'hours_sem3': hours_sem3,
        'hours_sem4': hours_sem4,
        'hours_sem5': hours_sem5,
        'hours_sem6': hours_sem6,
        'hours_sem7': hours_sem7,
        'hours_sem8': hours_sem8,
        
        'total_credits_s': total_credits_s,
        'total_hours_s': total_hours_s,
        
        'total_resources_sem1': total_resources_sem1,
        'total_resources_sem2': total_resources_sem2,
        'total_resources_sem3': total_resources_sem3,
        'total_resources_sem4': total_resources_sem4,
        'total_resources_sem5': total_resources_sem5,
        'total_resources_sem6': total_resources_sem6,
        'total_resources_sem7': total_resources_sem7,
        'total_resources_sem8': total_resources_sem8,
        'total_resources_all_sem': total_resources_all_sem,
    }

    return context
