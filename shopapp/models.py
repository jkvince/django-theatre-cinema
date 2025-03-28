from django.db import models
import uuid

from accounts.models import CustomUser

#class Order(models.Model):
#    order_id = models.UUIDField(primary_key=True)
#    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#    total = models.FloatField()
#    date_ordered = models.DateField(auto_now_add=True)
#
#    billing_name = models.CharField(max_length=250)
#    billing_address = models.CharField(max_length=250)
#    billing_city = models.CharField(max_length=250)
#    billing_postcode = models.CharField(max_length=10)
#    billing_country = models.CharField(max_length=50)