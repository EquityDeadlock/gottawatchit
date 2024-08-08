from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("content/<str:id>/", views.content, name="content"),
    path("register/", views.register, name="register"),
    path("create-media/", views.createMedia, name="create-media"),
    path("update-media/<str:id>/", views.updateMedia, name="update-media"),
    path("delete-media/<str:id>/", views.deleteMedia, name="delete-media"),
    path("create-tag/", views.createTag, name="create-tag"),
]
