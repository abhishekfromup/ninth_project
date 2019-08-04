from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ['student_id', 'student_name', 'student_email', 'student_date_of_birth', 'student_mobile']
# Register your models here.

admin.site.register(Student, StudentAdmin)