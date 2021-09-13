
from django.db import models
from shopapp.models import *
from django.template.defaultfilters import slugify
class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class item(models.Model):
    prodt=models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan= models.IntegerField()
    active=models.BooleanField(default=True)

    def total(self):
        return self.prodt.price*self.quan

    def __str__(self):
        return self.prodt
# Create your models here.
