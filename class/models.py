from django.db import models

# Create your models here.


class Class(models.Model):
    class_name = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,)
