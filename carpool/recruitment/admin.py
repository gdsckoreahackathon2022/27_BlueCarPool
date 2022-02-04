from django.contrib import admin
from .models import Recruit
# Register your models here.

class RecruitAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Recruit, RecruitAdmin)