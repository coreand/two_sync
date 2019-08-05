import requests
from django.contrib import admin
from django.forms import model_to_dict

from store.settings import WAREHOUSE_API, WAREHOUSE_USER, WAREHOUSE_PASS
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["order_number", "status"]
        else:
            return []

    def save_model(self, request, obj, form, change):
        data = model_to_dict(obj)

        resp = requests.post(f'http://{WAREHOUSE_API}/auth/',
                             data={'username': WAREHOUSE_USER, 'password': WAREHOUSE_PASS})
        token = resp.json()['token']

        headers = {'Authorization': f'Token {token}'}
        resp = requests.post(f'http://{WAREHOUSE_API}/orders/create/', data=data, headers=headers)
        if resp.status_code != 200:
            raise Exception(f'Error sending request to warehouse: {resp.content}')
        super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
