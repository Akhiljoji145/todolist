from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def add_task(request):
	if request.method=='POST':
		name=request.POST.get('name')
		priority=request.POST.get('priority')
		date=request.POST.get('date')
		redirect('/')
	else:	
		return render(request,'add.html')
