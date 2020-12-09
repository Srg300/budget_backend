from django.urls import path
from . import views

urlpatterns = [
    path('budget/', views.get_data),
    # path('glavbudget', views.get_glav_budget),
    # path('demo/', views.demo),
    ]
