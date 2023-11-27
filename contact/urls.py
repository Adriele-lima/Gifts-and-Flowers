from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success_page', views.contact_success_page, name='contact_success_page'),
]
