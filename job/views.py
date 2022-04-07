from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .serializers import AnnouncedJobsSerializers
from .models import AnnouncedJobs
# Create your views here.


class AnnouncedJobsView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AnnouncedJobsSerializers

    def get_queryset(self):
        jobs = AnnouncedJobs.objects.filter(job_confirm=True)
        return jobs
