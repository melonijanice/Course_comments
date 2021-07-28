from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_view),
    path('create',views.create),
    path('<int:id>/destroy',views.destroy),
    path('<int:id>/comment',views.comment)

    ]