from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from teacher import urls as teacherUrls
from .views import TeacherView, TeacherDetailview

urlpatterns = [
    # url('teacher-details/<int:pk>/', TeacherView.as_view(), name='teacher-details'),
    url('create-teacher/', TeacherView.as_view(), name='create-teacher'),
    url('teacher-details/<int:pk>', TeacherView.as_view(), name='teacher-details'),
    url('teacher-update/<pk>/', TeacherView.as_view(), name='teacher-update'),

]
