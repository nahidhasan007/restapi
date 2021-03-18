from django.urls import path
from . import views
from .views import index
from .views import TodoView

urlpatterns = [
    path('',index),
    path('view/',TodoView.as_view(),name=view),
]