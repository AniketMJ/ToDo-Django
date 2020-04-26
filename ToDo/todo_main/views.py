from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.all().order_by('-date_added')
    form = TodoForm()
    context = {
        'todo_list': todo_list,
        'form': form
    }
    return render(request, 'todo_main/index.html', context)


def add_todo(request):
    todo_list = Todo.objects.all().order_by('-date_added')

    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.author = request.user
            new_todo.save()
            return redirect('todo:index')
    else:
        form = TodoForm()

    context = {
        'todo_list': todo_list,
        'form': form
    }
    return render(request, 'todo_main/index.html', context)


def delete_todo(request, pk):
    todo_obj = get_object_or_404(Todo, pk=pk)
    todo_obj.delete()
    # path_info is a variable stored in request.
    # It has the current url that you're on. It's just like reloading the page.
    # return HttpResponseRedirect(request.path_info)  # delete/<pk>
    return redirect('todo:index')


def delete_completed(request):
    todo_objects = Todo.objects.filter(complete__exact=True)
    todo_objects.delete()

    return redirect('todo:index')


def delete_selected(request):
    user = get_object_or_404(User, username=request.user)
    pks = request.POST.getlist('selected')
    print(request.POST)
    # values_list() gives a list of rows,
    # each row a tuple of all of the fields you specify as arguments, in order.
    # If you only pass a single field in as an argument,
    # you can also specify flat=True to get a plain list instead of a list of tuples
    # todo_obj = Todo.objects.filter(
    #         author=request.user).values_list('pk', flat=True)
    for pk in pks:
        user_todo_ids = user.todo_set.all().values_list('pk', flat=True)
        if pk in user_todo_ids:
            todo_obj = user.todo_set.get(pk=pk)
            todo_obj.delete()

    return redirect('todo:index')


def complete_todo(request, pk):
    todo_obj = get_object_or_404(Todo, pk=pk)
    todo_obj.complete = not todo_obj.complete   # will give the opposite value
    todo_obj.save()

    return redirect('todo:index')


def complete_all(request):
    todos = Todo.objects.filter(complete__exact=False)
    for todo in todos:
        todo.complete = not todo.complete
        todo.save()

    return redirect('todo:index')


def complete_selected(request):
    user = get_object_or_404(User, username=request.user)
    pks = request.POST.getlist('selected')
    print(pks)
    for pk in pks:
        user_todo_ids = user.todo_set.all().values_list('pk', flat=True)
        if pk in user_todo_ids:
            todo_obj = user.todo_set.get(pk=pk)
            todo_obj.complete = True
            todo_obj.save()

    return redirect('todo:index')
