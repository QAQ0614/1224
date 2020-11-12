from django.urls import path 
from .views  import *

urlpatterns = [
    # path('poll/<int:pk>/', views.PollDetail.as_view()),
    path('poll/', PollList.as_view()),
    path('poll/<int:pk>/', PollDetail.as_view()),

]
