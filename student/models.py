# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField(unique=True, max_length=200)
    phone = models.CharField(max_length=10)
    section = models.CharField(max_length=1)
    is_active = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    join_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
