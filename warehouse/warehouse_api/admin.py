import requests
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import model_to_dict

from warehouse.settings import STORE_API
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
            resp = requests.post(f'http://{STORE_API}/orders/update/', data=data)
            if resp.status_code != 200:
                raise Exception(f'Error sending request to store: {resp.content}')
            super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
