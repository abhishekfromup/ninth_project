from django.db import models

# Create your models here.

class Student(models.Model):
	student_id = models.AutoField(primary_key = True)
	student_name = models.CharField(max_length = 30)
	student_email = models.EmailField(max_length = 30)
	student_date_of_birth = models.DateTimeField()
	student_mobile = models.CharField(max_length = 12)