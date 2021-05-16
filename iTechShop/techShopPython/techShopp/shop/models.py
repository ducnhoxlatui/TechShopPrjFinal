from django.db import models


# Create your models here.
class PGroup(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    pro_id = models.AutoField(primary_key='true')
    pro_name = models.CharField(max_length=255)
    group = models.ForeignKey(PGroup, on_delete=models.CASCADE)
    pro_price = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    pro_image = models.ImageField(upload_to='shop_images')  # phải install 3rd party package: Pillow

    def __str__(self):
        return self.pro_id.__str__()



class Customer(models.Model):
    cus_id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    mobile = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key='true')
    user_id = models.IntegerField()
    totmoney = models.IntegerField(default=0)
    def __str__(self):
        return self.order_id.__str__()

class OderDetail(models.Model):
    detail_id = models.AutoField(primary_key='true')
    order_id = models.IntegerField(null=False)
    pro_id = models.IntegerField(null=False)
    pro_price = models.IntegerField(null=False)
    pro_image = models.IntegerField()
    Quantity = models.IntegerField(null=False)
    status = models.IntegerField()
    def __str__(self):
        return self.detail_id.__str__()
