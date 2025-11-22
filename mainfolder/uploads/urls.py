from django.urls import path
from .views import upload_assignment

urlpatterns = [
    path('upload/', upload_assignment, name='upload'),
]
