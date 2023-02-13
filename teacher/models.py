from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .utils import unique_order_id_generator
# Create your models here.


class Teacher(models.Model):    
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    join_date = models.DateField()
    working_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)   

# def unique_code_generator(self, sender, instance, **kwargs):
#     if not instance.teacher_code:
#         instance.teacher_code = unique_order_id_generator(instance)


# pre_save.connect(unique_order_id_generator, sender=Teacher)


# @receiver(post_save, sender=Teacher)
# def post_save_receiver(sender, instance, created, **kwargs):
#     if created:
#         Teacher.objects.create(
#             full_name = instance.full_name
#         )
#     else:
#         Teacher.save()
