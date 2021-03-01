from django.contrib import admin
from django.urls import path

from .views import BloodAPIView
from .views import BloodCategoryAPIView
from .views import BloodDetailView
from .views import BloodNewView

urlpatterns = [

    path('',BloodCategoryAPIView.as_view()),
    path('blood/', BloodAPIView.as_view()),
    path('blood/<int:pk>/',BloodDetailView.as_view()),
    path('blood/new/',BloodNewView.as_view()),
]
