# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('index', views.index),
	path('cookies', views.cookies),
	path('home', views.home),
	path('get_record', views.get_record),
	path('name', views.name_view),
	path('age', views.age_view),
	path('email', views.email_view),
	path('result', views.result_view)
]