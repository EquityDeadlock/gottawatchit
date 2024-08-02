from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("content/<str:id>/", views.content, name="content")
]
