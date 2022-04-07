from django.urls import path
from .views import ApplicationsCreateApiView, PaymentApiVIEW
urlpatterns = [
	path('create', ApplicationsCreateApiView.as_view()),
	path('pay', PaymentApiVIEW.as_view())
]