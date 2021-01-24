from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path('login', views.login),
    path('logout', views.logut),
    path("news/new", views.createnews),
    path("news/<id>", views.shownews, name = 'news'),
    path("/news/<id>/edit", views.updatenews, name= 'edit'),
    path("/news/<id>/delete", views.deletenews, name= 'delete'),
]