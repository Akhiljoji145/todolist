from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TodoList
# Create your views here.
def add_task(request):
	if request.method=='POST':
		name=request.POST.get('name')
		priority=request.POST.get('priority')
		date=request.POST.get('date')
		task=TodoList(name=name,priority=priority,date=date)
		task.save()
		show_task=TodoList.objects.all()
		return render(request,'add.html',{'task':show_task})
	else:	
		task=TodoList.objects.all()
		return render(request,'add.html',{'task':task})
	
