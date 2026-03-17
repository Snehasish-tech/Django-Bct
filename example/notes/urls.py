from django.urls import path
from .views import notes

urlpatterns = [
    path('', notes, name='notes'),
]
