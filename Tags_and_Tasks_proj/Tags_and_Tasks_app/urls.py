
from django.urls import path

from .views import TaskListView, TagListView, TaskCreateView, TagCreateView, TagDeleteView, TaskDeleteView, \
    TagUpdateView, TaskUpdateView, TaskToggleView

app_name = 'practiceDjango'

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('tags', TagListView.as_view(), name='tags'),
    path('task_create', TaskCreateView.as_view(), name='task_create'),
    path('tag_create', TagCreateView.as_view(), name='tag_create'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
path(
  'task/<int:pk>/toggle/',
  TaskToggleView.as_view(),
  name='task-toggle'
),
]