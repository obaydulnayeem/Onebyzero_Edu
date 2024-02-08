# admin_panel/models.py

from django.db import models
from account.models import Profile

class AdminModel(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # Add other fields as needed

