from django.urls import path, include
from .views import CustomerView

urlpatterns = [
	path('', include('djoser.urls')),
	path('', include('djoser.urls.jwt')),
	path('profile', CustomerView.as_view())
]