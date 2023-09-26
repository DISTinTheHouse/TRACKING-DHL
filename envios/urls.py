from django.urls import path
from . import views
from .views import get_shipment_status

urlpatterns = [
    path('envios', views.envios, name="envios"),
    path('get-shipment-status/', get_shipment_status, name='get_shipment_status'),
]

