from django.db import models


class Order(models.Model):
    STATUSES = ['New', 'In progress', 'Stored', 'Sent']
    STATUSES_ENUM = [(idx, status) for idx, status in enumerate(STATUSES)]

    order_number = models.CharField(max_length=255, verbose_name='Order number')
    status = models.IntegerField(choices=STATUSES_ENUM, verbose_name='Status')

    def __str__(self):
        status = None if self.status is None else self.STATUSES[self.status]
        return f'{self.order_number} -> {status}'
