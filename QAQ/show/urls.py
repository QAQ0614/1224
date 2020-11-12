from django.urls import path
from . import views

urlpatterns = [
  path('food/<int:kind>', views.food),
]