from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('results/', views.results),
    path('domain/<int:id>/', views.domain_detail),
    path('dashboard/', views.dashboard),
]