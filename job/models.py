from django.db import models

# Create your models here.
from django.db import models

class DegreeEnum(models.IntegerChoices):
    MATRIC = 1, 'MATRIC or more'
    FSC = 2, 'FSC or more'
    BS = 3, 'BS or more'
    MS = 4, 'MS or more'

class ExperienceEnum(models.IntegerChoices):
    ONE = 1, 'ONE or more'
    TWO = 2, 'TWO or more'
    THREE = 3, 'THREE or more'
    FOUR = 4, 'FOUR or more'


class AnnouncedJobs(models.Model):
	is_active_job = models.BooleanField(default=True)
	position_title = models.CharField(max_length=256)
	experienced = models.CharField(max_length=256)
	qualification = models.CharField(max_length=256)
	knowledge = models.CharField(max_length=256)
	job_responsibility = models.CharField(max_length=256)
	skill_set = models.CharField(max_length=256)
	description = models.TextField()

	Degree = models.SmallIntegerField(choices=DegreeEnum.choices)
	experience = models.IntegerField(choices=ExperienceEnum.choices)

	def __int__(self):
		return self.position_title

	class Meta:
		verbose_name = 'Jobs'