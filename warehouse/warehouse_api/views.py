from rest_framework import generics
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_number = serializer.validated_data['order_number']
        status = serializer.validated_data['status']
        Order.objects.create(order_number=order_number, status=status)

        return Response({'status': 'ok'})
