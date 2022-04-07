from django.contrib import admin
from .models import AnnouncedJobs
# Register your models here.

class AnnouncedJobsAdmin(admin.ModelAdmin):
	list_display = [
		'position_title',
		'Degree',
		'experience',
		'is_active_job'
	]

admin.site.register(AnnouncedJobs, AnnouncedJobsAdmin)