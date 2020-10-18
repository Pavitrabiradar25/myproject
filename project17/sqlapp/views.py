from django.shortcuts import render
from sqlapp.models import studyonlinetable

def home_page(request):
	return render(request=request,template_name='sqlapp/homepage.html')

def display_data(request):
	student_data=studyonlinetable.objects.all()
	print(student_data)
	print(type(student_data))

	my_dict={'student_data':student_data}

	return render(request=request,template_name='sqlapp/display.html',context=my_dict)
