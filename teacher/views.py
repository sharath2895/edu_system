from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TeacherSerializer
from .models import Teacher as TeacherModel
# Create your views here.


class TeacherView(generics.GenericAPIView):
    serializer_class = TeacherSerializer()
    teacher_model = TeacherModel.objects.all()
    lookup_field = 'pk'

    # def get(self, request, pk):
    #     print(pk)
    #     print("get request")
    #     return Response(data={"hello"}, status=status.HTTP_200_OK)

    def get(self, request, pk):
        print(pk)
        # return Response(data={"message"}, status=status.HTTP_200_OK)
        print(self.kwargs.get('pk'))
        self.teacher_data = TeacherModel.objects.filter(pk=pk)
        print(self.teacher_data)
        try:
            if self.teacher_data:
                self.serializer_class_data = TeacherSerializer(
                    data=self.teacher_data)
                return Response(data=self.serializer_class_data.data, status=status.HTTP_200_OK)
            else:
                return Response(data=self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise Exception(Exception)

    def post(self, request):
        data = request.data
        serializer_class = TeacherSerializer(data=data)
        print(serializer_class, 'serializer data')
        try:
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(data=serializer_class.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise Exception()

    def put(self, request, pk):
        print(request)
        self.teacher_data = TeacherModel.objects.get(pk=pk)

        self.serializer_class = TeacherSerializer(
            self.teacher_data, request.data)

        if self.serializer_class.is_valid():
            self.serializer_class.save()
            return Response(data=self.serializer_class.data, status=status.HTTP_200_OK)
        else:
            return Response(data=self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailview(APIView):
    def get(self, request,pk):
        print(pk)
        return Response(data={"message"}, status=status.HTTP_200_OK)
