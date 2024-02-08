# admin_panel/admin.py

from django.contrib import admin
from .models import AdminModel

admin.site.register(AdminModel)
# Add other model registrations and customizations as needed
