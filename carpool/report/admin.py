from django.contrib import admin
from .models import Report



class ReportAdmin(admin.ModelAdmin):
    search_fields=['subject']

admin.site.register(Report,ReportAdmin)

