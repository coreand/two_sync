import requests
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import model_to_dict

from warehouse.settings import STORE_API, STORE_USER, STORE_PASS
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["order_number"]
        else:
            return ["order_number", "status"]

    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()
        except ValidationError:
            super().save_model(request, obj, form, change)
        else:
            data = model_to_dict(obj)

            resp = requests.post(f'http://{STORE_API}/auth/',
                                 data={'username': STORE_USER, 'password': STORE_PASS})
            token = resp.json()['token']

            headers = {'Authorization': f'Token {token}'}
            resp = requests.post(f'http://{STORE_API}/orders/update/', data=data, headers=headers)
            if resp.status_code != 200:
                raise Exception(f'Error sending request to store: {resp.content}')
            super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
