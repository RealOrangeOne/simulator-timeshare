from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('submit/', views.CreateSimulationView.as_view()),
    path('<int:pk>/', views.SimulationDetailView.as_view())
]
