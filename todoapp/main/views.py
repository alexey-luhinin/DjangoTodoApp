from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TodoForm()
    todo_complete = Todo.objects.filter(is_done=True).order_by('-id')
    todo_incomplete = Todo.objects.filter(is_done=False).order_by('-id')
    return render(request, 'main/index.html', 
            {'todo_complete': todo_complete, 
             'todo_incomplete': todo_incomplete,
             'form':form})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_done = True
    todo.save()
    return redirect('index')

