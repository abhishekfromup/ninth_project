from django.shortcuts import render
from .forms import StudentForm
from .models import *
# Create your views here.

def index(request):
	form = StudentForm()
	if request.method == 'POST':
		form = StudentForm(request.POST)
		# print('__________________if')
		if form.is_valid():
			name = form.cleaned_data['student_name']
			email = form.cleaned_data['student_email']
			dob = form.cleaned_data['student_date_of_birth']
			mobile = form.cleaned_data['student_mobile']

			# print("+++++"+ str(latest_id.student_id) + "_______________")
			s = Student(Student.objects.last().student_id+1, name, email, dob, mobile)
			s.save()
			return home(request)
			# print("--------Data saved")
	return render(request, 'ninth_app/index.html', {'form': form.as_p})

def home(request):
	return render(request, 'ninth_app/home.html')

def get_record(request):
	student_record = Student.objects.all()
	my_dict = {'record': student_record}
	return render(request, 'ninth_app/get_record.html', context = my_dict)
