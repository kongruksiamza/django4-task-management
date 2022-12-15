from django.urls import path
from taskapp import views

urlpatterns=[
    path('',views.index),
    path('completed/<task_id>',views.complete_task,name="completed"),
    path('pending/<task_id>',views.pending_task,name="pending")
]