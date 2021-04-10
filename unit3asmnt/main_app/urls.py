from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widgets/', views.create, name="create"),
    path('widgets/<int:widget_id>/', views.delete, name="delete"),
]