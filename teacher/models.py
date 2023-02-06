from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_code = models.CharField(max_length=20)
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    join_date = models.DateField()
    working_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

   
