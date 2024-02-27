# from study.models import Question, BookModel, NoteModel, LectureModel
# from account.models import Profile
# from django.utils import timezone
# from django.utils.timezone import now

# def format_upload_time(upload_time):
#     current_time = timezone.now()
#     duration = current_time - upload_time
#     seconds_ago = duration.total_seconds()

#     def pluralize(value, unit):
#         if value == 1:
#             return f"{value} {unit}"
#         else:
#             return f"{value} {unit}s"

#     if seconds_ago < 60:
#         return pluralize(int(seconds_ago), "second") + " ago"
#     elif seconds_ago < 3600:
#         return pluralize(int(seconds_ago/60), "minute") + " ago"
#     elif seconds_ago < 86400:
#         return pluralize(int(seconds_ago/3600), "hour") + " ago"
#     elif seconds_ago < 604800:
#         return pluralize(int(seconds_ago/86400), "day") + " ago"
#     elif seconds_ago < 2419200:
#         return pluralize(int(seconds_ago/604800), "week") + " ago"
#     elif seconds_ago < 29030400:
#         return pluralize(int(seconds_ago/2419200), "month") + " ago"
#     else:
#         return pluralize(int(seconds_ago/29030400), "year") + " ago"

# def recent_uploads_view(request):
#     latest_question = Question.objects.last()
#     # print(latest_question)
#     uploader_latest_question = latest_question.uploaded_by.nickname
#     upload_time_latest_question = latest_question.upload_time
#     # upload_time_latest_question = now()
#     formatted_time_latest_question = format_upload_time(upload_time_latest_question)

#     latest_book = BookModel.objects.last()
#     uploader_latest_book = latest_book.uploaded_by.nickname
#     upload_time_latest_book = latest_book.upload_time
#     formatted_time_latest_book = format_upload_time(upload_time_latest_book)
    
#     latest_note = NoteModel.objects.last()
#     uploader_latest_note = latest_note.uploaded_by.nickname
#     upload_time_latest_note = latest_note.upload_time
#     formatted_time_latest_note = format_upload_time(upload_time_latest_note)
    
#     latest_lecture = LectureModel.objects.last()
#     uploader_latest_lecture = latest_lecture.uploaded_by.nickname
#     upload_time_latest_lecture = latest_lecture.upload_time
#     formatted_time_latest_lecture = format_upload_time(upload_time_latest_lecture)
        
#     context = {
#         'uploader_latest_question': uploader_latest_question,
#         'latest_question': latest_question,
#         'formatted_time_latest_question': formatted_time_latest_question,
        
#         'uploader_latest_book': uploader_latest_book,
#         'latest_book': latest_book,
#         'formatted_time_latest_book': formatted_time_latest_book,

#         'uploader_latest_note': uploader_latest_note,
#         'latest_note': latest_note,
#         'formatted_time_latest_note': formatted_time_latest_note,

#         'uploader_latest_lecture': uploader_latest_lecture,
#         'latest_lecture': latest_lecture,
#         'formatted_time_latest_lecture': formatted_time_latest_lecture
#     }

#     return context