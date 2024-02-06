from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TodoList
from .forms import TodoForm
# Create your views here.
def add_task(request):
	if request.method=='POST':
		name=request.POST.get('name')
		priority=request.POST.get('priority')
		date=request.POST.get('date')
		task=TodoList(name=name,priority=priority,date=date)
		task.save()
		show_task=TodoList.objects.all()
		return redirect('/')
	else:	
		task=TodoList.objects.all()
		return render(request,'add.html',{'task':task})
	
def delete(request,task_id):
	todo=TodoList.objects.get(id=task_id)
	todo.delete()
	return redirect('/')

def update(request,task_id):
	todo=TodoForm()