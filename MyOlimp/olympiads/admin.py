from django.contrib import admin
from .models import *


class OlympiadAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'olympiad_level']
    list_filter = ['name', 'subject', 'olympiad_level']


admin.site.register(OlympiadSubjectGroup)
admin.site.register(OlympiadSubject)
admin.site.register(Olympiad, OlympiadAdmin)
