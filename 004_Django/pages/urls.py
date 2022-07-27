from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name="About"),
    path('singup', views.about, name="singup"),
]





