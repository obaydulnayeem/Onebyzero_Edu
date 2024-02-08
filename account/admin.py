from django.contrib import admin
from .models import Profile, PendingUserModel

# admin.site.register(Profile)
admin.site.register(PendingUserModel)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'university', 'department']
    
admin.site.register(Profile, ProfileAdmin)