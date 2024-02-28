from django.db import models
from django.contrib.auth.models import User
# from study.models import Department, University
from study.choices import SESSION_CHOICES, DEPARTMENTAL_BATCHES, SEMESTER_CHOICES

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('batch_ambassador', 'Batch Ambassador'),
        ('departmental_ambassador', 'Departmental Ambassador'),
        ('university_ambassador', 'University Ambassador'),
        ('admin', 'Admin'),
    )
    
    YEAR_CHOICES = (
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
    )
    
    # SEM_CHOICES = (
    #     (1, '1st'),
    #     (2, '2nd'),
    # )
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, blank = True, null = True)
    # is_departmental_ambassador = models.ForeignKey('study.Department', on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    # profile_image = models.ImageField(upload_to='profile_images/', default = 'profile_images/default.png')
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png', blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True)
    university = models.ForeignKey('study.University', on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey('study.Department', on_delete=models.CASCADE, blank=True, null=True)
    session = models.CharField(max_length=50, choices=SESSION_CHOICES, blank=True, null=True)
    departmental_batch = models.CharField(max_length=50, choices=DEPARTMENTAL_BATCHES, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    # semester = models.CharField(max_length=50, blank=True, null=True, choices=SEMESTER_CHOICES)
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    facebook_id = models.CharField(max_length=100, blank=True)
    codeforces_id = models.CharField(max_length=100, blank=True)
    
    last_updated  = models.DateTimeField(auto_now=True)
    
 
    # import os
    # def update_profile_image_from_oauth(self, backend, response):
    #         url = None
    #         if backend.name == 'facebook':
    #             url = "http://graph.facebook.com/%s/picture?type=large" % response.get('id')
    #         elif backend.name == 'twitter':
    #             url = response.get('profile_image_url', '').replace('_normal', '')
    #         elif backend.name == 'google-oauth2':
    #             url = response.get('picture')

    #         if url:
    #             # Download the image and save it to the profile_image field
    #             # Here, you need to write code to download the image from the URL and save it to the profile_image field
    #             # Example:
    #             from django.core.files import File
    #             import urllib.request
    #             result = urllib.request.urlretrieve(url)
    #             self.profile_image.save(
    #                 os.path.basename(url),
    #                 File(open(result[0], 'rb'))
    #             )
    #             self.profile_image = url
    #             self.save()
            
# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver

# @receiver(user_logged_in)
# def update_profile_image(sender, user, request, **kwargs):
#     if user.is_authenticated:
#         # Assuming you have the authentication backend and response available
#         # Call the method to update the profile image
#         profile = user.profile  # Assuming Profile is related to User
#         profile.update_profile_image_from_oauth(backend, response)


class PendingUserModel(models.Model):
    # profile_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # requested_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.user.username} - {self.requested_at}"