# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class StudentListView(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        students = Student.objects.all()
        return students

    def get(self, request):
        students_list = self.get_queryset()
        serializer_data = StudentSerializer(students_list, many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        student_data = request.data
        serializer_data = StudentSerializer(data=student_data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(data=serializer_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get(self, request, pk):
        self.request = request
        students_detail = Student.objects.get(pk=pk)
        serializer = self.serializer_class(students_detail)
        try:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data=serializer.errors, status=status.HTTP_200_OK)

    def put(self, request, pk):
        print(request.data)
        student_detail = Student.objects.filter(pk=pk)
        serializer_data = self.serializer_class(student_detail,request.data, many= True)

        if student_detail:
            if serializer_data.is_valid():
                serializer_data.save()
                return Response(data=serializer_data.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer_data.errors, status=status.HTTP_404_NOT_FOUND)
