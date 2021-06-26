from django.urls import path
from services import views as services_views

urlpatterns = [
    path('', services_views.services_list, name='services'),
]
