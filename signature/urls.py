from django.urls import path
from .views import upload_signature

urlpatterns = [
    path('upload/', upload_signature, name='upload_signature'),
]
