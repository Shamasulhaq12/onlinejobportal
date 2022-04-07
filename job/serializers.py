from rest_framework import serializers
from .models import AnnouncedJobs

class AnnouncedJobsSerializers(serializers.ModelSerializer):
	class Meta:
		model = AnnouncedJobs
		fields = [
			'id',
			'position_title',
			'experienced',
			'qualification',
			'knowledge',
			'job_responsibility',
			'skill_set',
			'description',
		]