from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from .views import StudentListView, StudentDetailView


urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),   
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
