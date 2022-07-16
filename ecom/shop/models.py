from django.db import models
# Create your models here.



class Product(models.Model):
    objects = None
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    objects = None
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    objects = None
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    name = models.CharField(max_length=50,default="Anonymous")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name+","+self.update_desc[0:7] + "...."
