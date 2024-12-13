from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def tasks_list(request):
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/list.html', ctx)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    ctx = {'task': task}
    return render(request, 'tasks/detail.html', ctx)

def task_create(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        if task_title and description and due_date:
            Task.objects.create(
                task_title=task_title,
                description=description,
                due_date=due_date

            )
            return redirect('tasks:list')
    return render(request, 'tasks/form.html')


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        if task_title and description and due_date:
            task.task_title = task_title,
            task.description = description,
            task.due_date = due_date,
            task.save()
            return redirect(task.get_detail_url())
    ctx = {'task': task}
    return render(request, 'tasks/form.html', ctx)
