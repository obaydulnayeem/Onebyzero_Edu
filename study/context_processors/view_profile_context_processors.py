from study.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
    
def view_profile_contributions(request):
    # user_id = 2
    # user = get_object_or_404(User, pk=user_id)
    
    # user = get_object_or_404(User, pk=request.resolver_match.kwargs['user_id'])

    user_id = request.GET.get('user_id')
    print(f'user_idddddddddddddddd', user_id)
    # user = get_object_or_404(User, pk=user_id)

    if user_id:
        # Retrieve the user based on user_id
        user = get_object_or_404(User, user_id=user_id)
        return {'user': user}
    else:
        return {}

# QUESTIONS ========================================
    qs_sem1_others = Question.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    qs_sem2_others = Question.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    qs_sem3 = Question.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    qs_sem4 = Question.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    qs_sem5 = Question.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    qs_sem6 = Question.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    qs_sem7 = Question.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    qs_sem8 = Question.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    qs_total = qs_sem1_others + qs_sem2_others + qs_sem3 + qs_sem4 + qs_sem5 + qs_sem6 + qs_sem7 + qs_sem8
    

# BOOKS ==============================================
    books_sem1 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    books_sem2 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    books_sem3 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    books_sem4 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    books_sem5 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    books_sem6 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    books_sem7 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    books_sem8 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    books_total = books_sem1 + books_sem2 + books_sem3 + books_sem4 + books_sem5 + books_sem6 + books_sem7 + books_sem8
    

# LECTURE SLIDES ============================================
    lectures_sem1 = LectureModel.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    lectures_sem2 = LectureModel.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    lectures_sem3 = LectureModel.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    lectures_sem4 = LectureModel.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    lectures_sem5 = LectureModel.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    lectures_sem6 = LectureModel.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    lectures_sem7 = LectureModel.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    lectures_sem8 = LectureModel.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    lectures_total = lectures_sem1 + lectures_sem2 + lectures_sem3 + lectures_sem4 + lectures_sem5 + lectures_sem6 + lectures_sem7 + lectures_sem8
    
    
# NOTES =============================================
    notes_sem1 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    notes_sem2 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    notes_sem3 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    notes_sem4 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    notes_sem5 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    notes_sem6 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    notes_sem7 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    notes_sem8 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    notes_total = notes_sem1 + notes_sem2 + notes_sem3 + notes_sem4 + notes_sem5 + notes_sem6 + notes_sem7 + notes_sem8
    
    # TOTAL UPLOADS ==================
    total_uploads = sum([qs_total, books_total, lectures_total, notes_total], 0)
    
    # TOTALS UPLOADS SEMESTER WISE
    all_sem1 = sum([qs_sem1_others, books_sem1, lectures_sem1, notes_sem1], 0)
    all_sem2 = sum([qs_sem2_others, books_sem2, lectures_sem2, notes_sem2], 0)
    all_sem3 = sum([qs_sem3, books_sem3, lectures_sem3, notes_sem3], 0)
    all_sem4 = sum([qs_sem4, books_sem4, lectures_sem4, notes_sem4], 0)
    all_sem5 = sum([qs_sem5, books_sem5, lectures_sem5, notes_sem5], 0)
    all_sem6 = sum([qs_sem6, books_sem6, lectures_sem6, notes_sem6], 0)
    all_sem7 = sum([qs_sem7, books_sem7, lectures_sem7, notes_sem7], 0)
    all_sem8 = sum([qs_sem8, books_sem8, lectures_sem8, notes_sem8], 0)
    
    
    context = {
        'qs_sem1_others': qs_sem1_others,
        'qs_sem2_others': qs_sem2_others,
        'qs_sem3': qs_sem3,
        'qs_sem4': qs_sem4,
        'qs_sem5': qs_sem5,
        'qs_sem6': qs_sem6,
        'qs_sem7': qs_sem7,
        'qs_sem8': qs_sem8,
        'qs_total': qs_total,
        
        'books_sem1': books_sem1,
        'books_sem2': books_sem2,
        'books_sem3': books_sem3,
        'books_sem4': books_sem4,
        'books_sem5': books_sem5,
        'books_sem6': books_sem6,
        'books_sem7': books_sem7,
        'books_sem8': books_sem8,
        'books_total': books_total,
        
        'lectures_sem1': lectures_sem1,
        'lectures_sem2': lectures_sem2,
        'lectures_sem3': lectures_sem3,
        'lectures_sem4': lectures_sem4,
        'lectures_sem5': lectures_sem5,
        'lectures_sem6': lectures_sem6,
        'lectures_sem7': lectures_sem7,
        'lectures_sem8': lectures_sem8,
        'lectures_total': lectures_total,
        
        'notes_sem1': notes_sem1,
        'notes_sem2': notes_sem2,
        'notes_sem3': notes_sem3,
        'notes_sem4': notes_sem4,
        'notes_sem5': notes_sem5,
        'notes_sem6': notes_sem6,
        'notes_sem7': notes_sem7,
        'notes_sem8': notes_sem8,
        'notes_total': notes_total,
        
        'total_uploads': total_uploads,
        
        'all_sem1': all_sem1,
        'all_sem2': all_sem2,
        'all_sem3': all_sem3,
        'all_sem4': all_sem4,
        'all_sem5': all_sem5,
        'all_sem6': all_sem6,
        'all_sem7': all_sem7,
        'all_sem8': all_sem8,
        
        'view_profile_user': user,
        # 'user': user,
    }
    
    return context
