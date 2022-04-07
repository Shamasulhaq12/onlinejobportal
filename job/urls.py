from django.urls import path
from .views import AnnouncedJobsView

urlpatterns = [
	path('jobs', AnnouncedJobsView.as_view())
]