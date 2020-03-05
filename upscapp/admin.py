from django.contrib import admin
from .models import ServicesData, Post, Comment


class AdminServicesData(admin.ModelAdmin):

  list_display = ['subject_code',
                  'subject_name',
                  'subject_duration',
                  'subject_startdate',
                  'subject_starttime',
                  'subject_instructor_name',
                  'subject_instructor_experience']


admin.site.register(ServicesData, AdminServicesData)
admin.site.register(Post)
admin.site.register(Comment)