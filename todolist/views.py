from django.shortcuts import render, HttpResponse,redirect
from .forms import TaskForm
from .models import Task
from django.views import View
from django.views.generic import UpdateView

# Create your views here.

# 1
# def index(request):
#     # return HttpResponse("Hello World!!")
#     form = TaskForm()
#     return render(request, "todolist/index.html", {"task_form": form})

# 2  is_valid
# def index(request):
#     # return HttpResponse("Hello World!!")
#     form = TaskForm()
#     if request.method == "POST":
#         #Get the posted form
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     return render(request, "todolist/index.html", {"task_form": form})  


# 3
# Retrieve/Display Task
def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    tasks = Task.objects.all() # add this
    return render(request, "todolist/index.html", {"task_form": form, "tasks": tasks})

class UpdateTaskView(View):
    def get_object(self, pk):
        task = Task.objects.get(id=pk)
        return task

    def get(self, request, pk):
        form = TaskForm(instance=self.get_object(pk))
        return render(request, "todolist/update_task.html", {"task_edit_form": form})

    def post(self,request, pk):
        form = TaskForm(request.POST, instance=self.get_object(pk))
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, "todolist/update_task.html", {"task_edit_form": form})
        

class UpdateTaskGenericView(UpdateView):
    form_class = TaskForm
    template_name = "todolist/update_task.html"
    model = Task

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        form = TaskForm(instance=self.get_object())
        context = {'task_edit_form': form}
        return context

# update
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'GET':
        form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "todolist/update_task.html", {"task_edit_form": form})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")