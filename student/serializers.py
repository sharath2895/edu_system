from .models import Student


from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
    # def create(self, validated_data):
    #     student_serializer = StudentSerializer(data=validated_data)
    #     if student_serializer.is_valid():
    #         student_serializer.save()
    #         return Student.objects.create(**validated_data)
    #     else:
    #         raise Exception("Method cannot create Student")
