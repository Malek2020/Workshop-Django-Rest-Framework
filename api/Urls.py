from django.urls import path
from Views import *

urlpatterns = [
    path('events/', EventList.as_view()),
    path('add/', addEvent),
    path('delete/<int:id>/', deleteEvent),
    path('update/<int:id>/', updateEvent),
]
