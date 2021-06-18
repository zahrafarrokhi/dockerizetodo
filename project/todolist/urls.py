from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/<int:pk>/", views.UpdateTaskGenericView.as_view(), name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"), #this
]