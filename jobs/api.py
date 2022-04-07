from django.urls import path, include

urlpatterns = [
	# path('hod/', include('hod.urls')),
	path('get/', include('job.urls')),
	path('user/', include('user.urls')),
	path('applications/', include('applications.urls')),
]