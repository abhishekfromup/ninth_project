from django.shortcuts import render
from .forms import *
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

def cookies(request):
	count = int(request.COOKIES.get('count', 0))
	# print("+++++++++++request.COOKIES++++++++++++++++++")
	# print(request.COOKIES)
	# print("+++++++++++++++++++++++++++++")
	# print("+++++++++++request.COOKIES++++++++++++++++++")
	# print(dir(request))
	# print("+++++++++++++++++++++++++++++")

	new_count = count + 1
	response = render(request, 'ninth_app/cookies.html', {'count': new_count})
	# print("+++++++++++++++++++++++++++++")
	# print(dir(response))
	# print("+++++++++++++++++++++++++++++")
	response.set_cookie('count', new_count)
	# print("_____________________________")
	# print(dir(response))
	# print("_____________________________")

	return response

def name_view(request):
	form = Name()
	my_dict = {'form': form.as_p}
	response = render(request, 'ninth_app/name.html', my_dict)
	return response

def age_view(request):
	name = request.GET['name']
	cook_name = request.COOKIES.get('name', 'no name!')
	form = Age()
	my_dict = {'form':form.as_p, 'name': name, 'cook_name': cook_name}
	response = render(request, 'ninth_app/age.html', my_dict)
	response.set_cookie('name', name)
	return response

def email_view(request):
	age = request.GET['age']
	form = Email()
	my_dict = {'form': form, 'age': age}
	response = render(request, 'ninth_app/email.html', my_dict)
	response.set_cookie('age', age)
	return response

def result_view(request):
	email = request.GET['email']
	name = request.COOKIES.get('name', '!!!no name!!!')
	age = request.COOKIES.get('age', '!!! no age !!!')
	email = request.COOKIES.get('email', '!!! no email !!!')
	
	my_dict = {
		'name': name,
		'age': age,
		'email': email
	}

	response = render(request, 'ninth_app/result.html', my_dict)
	return response