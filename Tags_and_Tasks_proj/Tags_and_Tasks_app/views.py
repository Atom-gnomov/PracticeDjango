from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView

from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'main.html'


class TagListView(ListView):
    model = Tag
    context_object_name = 'tag_list'
    template_name = 'tag.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['content', 'deadline', 'done', 'tags']
    template_name = 'task_create.html'
    success_url = reverse_lazy('practiceDjango:index')


class TagCreateView(CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'tags_create.html'
    success_url = reverse_lazy('practiceDjango:tags')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    # after deletion, go back to the task list
    success_url = reverse_lazy('practiceDjango:index')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tag_confirm_delete.html'

    success_url = reverse_lazy('practiceDjango:tags')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['content', 'deadline', 'done', 'tags']
    template_name = 'task_form.html'
    success_url = reverse_lazy('practiceDjango:index')


class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'
    template_name = 'tag_form.html'
    success_url = reverse_lazy('practiceDjango:tags')

class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        new_state = request.POST.get('done') == 'true'
        task.done = new_state
        task.save()
        return redirect('practiceDjango:index')