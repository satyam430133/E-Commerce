from django.urls import path
from .views import *

urlpatterns = [
    path('',Cards.as_view(),name='cards'),
]