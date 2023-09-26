from django.shortcuts import render
from django.http import JsonResponse
import requests
import hashlib
import hmac
import base64

def envios(request): #Index de envios
    return render(request, 'envios.html')

def get_shipment_status(request):
    API_KEY = 'KZrV16elrMpgDIcUvpsAd7JGleGCHICI'
    BASE_URL = 'https://api-eu.dhl.com/track/shipments'

    if request.method == 'GET':
        tracking_id = request.GET.get('tracking_id')

        headers = {
            'DHL-API-Key': API_KEY,
        }

        params = {
            'trackingNumber': tracking_id,
        }

        try:
            response = requests.get(BASE_URL, params=params, headers=headers)
            data = response.json()
            return JsonResponse(data, safe=False)
        except requests.exceptions.RequestException as e:
            error_message = {'error': str(e)}
            return JsonResponse(error_message, status=500)

def search_shipment(request):
    return render(request, 'tracking_form.html')
