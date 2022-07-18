
from django.urls import path
from core.views import main, form

urlpatterns = [
    path("", main, name='main'),
    path("form", form, name='form'),
]