from django.urls import path
from . import views

urlpatterns = [
    path('django', views.django_intro, name='django'),
    path('display', views.display_process, name='display'),
    path('templates', views.template_engine, name='templates'),
]