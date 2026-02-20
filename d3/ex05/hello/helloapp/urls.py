from django.urls import path
from . import views
urlpatterns = [
    path('helloworld/', views.helloword, name='helloword'),
]