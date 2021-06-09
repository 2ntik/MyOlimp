from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'grade']
    list_filter = ['grade', 'sex', 'age']
    search_fields = ['user', 'school', 'third_name']


admin.site.register(City)
admin.site.register(School)
admin.site.register(Profile, ProfileAdmin)
