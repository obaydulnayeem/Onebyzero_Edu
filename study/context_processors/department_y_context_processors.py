from study.models import Department
from study.models import Course
from django.db.models import Sum

def department_y_context_view(request):
    # user = request.user.id
    department_id = None

    # Assuming department_id is passed in the URL, for example: /department/1/
    if 'department_id' in request.resolver_match.kwargs:
        department_id = request.resolver_match.kwargs['department_id']

    total_courses_y = Course.objects.filter(department = department_id).count()

    # TOTAL COURSES - YEAR WISE==========================
    courses_year1 = Course.objects.filter(department = department_id, year=1).count()
    courses_year2 = Course.objects.filter(department = department_id, year=2).count()
    courses_year3 = Course.objects.filter(department = department_id, year=3).count()
    courses_year4 = Course.objects.filter(department = department_id, year=4).count()
    
    
    # TOTAL CREDITS YEAR WISE===============================
    credits_year1 = Course.objects.filter(department = department_id, year=1).aggregate(total_credits_y=Sum('credit'))['total_credits_y'] or 0
    
    credits_year2 = Course.objects.filter(department = department_id, year=1).aggregate(total_credits_y=Sum('credit'))['total_credits_y'] or 0
    
    credits_year3 = Course.objects.filter(department = department_id, year=2).aggregate(total_credits_y=Sum('credit'))['total_credits_y'] or 0
    
    credits_year4 = Course.objects.filter(department = department_id, year=2).aggregate(total_credits_y=Sum('credit'))['total_credits_y'] or 0

    total_credits_y = credits_year1 + credits_year2 + credits_year3 + credits_year4
   
    # TOTAL HOURS YEAR WISE===============================
    hours_year1 = Course.objects.filter(department = department_id, year=1).aggregate(total_hours_y=Sum('hour'))['total_hours_y'] or 0
    
    hours_year2 = Course.objects.filter(department = department_id, year=1).aggregate(total_hours_y=Sum('hour'))['total_hours_y'] or 0
    
    hours_year3 = Course.objects.filter(department = department_id, year=2).aggregate(total_hours_y=Sum('hour'))['total_hours_y'] or 0
    
    hours_year4 = Course.objects.filter(department = department_id, year=2).aggregate(total_hours_y=Sum('hour'))['total_hours_y'] or 0
    
    total_hours_y = hours_year1 + hours_year2 + hours_year3 + hours_year4
    
    context = {
        'total_courses_y': total_courses_y,

        'courses_year1': courses_year1,
        'courses_year2': courses_year2,
        'courses_year3': courses_year3,
        'courses_year4': courses_year4,
        
        
        'credits_year1': credits_year1,
        'credits_year2': credits_year2,
        'credits_year3': credits_year3,
        'credits_year4': credits_year4,
        
        'hours_year1': hours_year1,
        'hours_year2': hours_year2,
        'hours_year3': hours_year3,
        'hours_year4': hours_year4,
        
        'total_credits_y': total_credits_y,
        'total_hours_y': total_hours_y,
    }

    return context
