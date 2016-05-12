from django.shortcuts import render
from .models import todo
from django.utils import timezone
from .forms import TodoForm

def todo_list(request):
    todos =  todo.objects.all().order_by('deadline')
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_new(request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid() :
			post = form.save(commit=False)
			post.save()
			todos =  todo.objects.all().order_by('deadline')
			return render(request, 'todo/todo_list.html', {'todos':todos})
	form = TodoForm()
	return render(request, 'todo/todo_new.html',{'form': form})

def todo_remove(request, pk):
    td=todo.objects.get(pk=pk)
    td.delete()
    todos =  todo.objects.all().order_by('deadline')
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_edit(request,pk):
	try:
		td=todo.objects.get(pk=pk)
	except td.DoesNotExist:
		return render(request, 'todo/todo_list.html', {'todos':todos})
	
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid() :
			post = form.save(commit=False)
			post.save()
			td.delete()
			todos =  todo.objects.all().order_by('deadline')
			return render(request, 'todo/todo_list.html', {'todos':todos})
	form = TodoForm(request.POST or None, instance=td)
	return render(request, 'todo/todo_edit.html', {'form': form, 'td':todo})

def todo_impressum(request):
	return render(request, 'todo/impressum.html', {})

















# Create your views here.
