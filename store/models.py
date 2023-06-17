from django.db import models


# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    category_description =  models.CharField(max_length=255)
    category_image = models.ImageField(max_length=200)

class Cart(models.Model):   
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(max_length=200)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)



class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
       
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    total_amount = models.DecimalField(max_digits=6,decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Order_details(models.Model):
    ITEM_STATUS_PENDING = 'P'
    ITEM_STATUS_COMPLETE = 'C'
    ITEM_STATUS_FAILED = 'F'
    ITEM_STATUS_CHOICES = [
        (ITEM_STATUS_PENDING, 'Pending'),
        (ITEM_STATUS_COMPLETE, 'Complete'),
        (ITEM_STATUS_FAILED, 'Failed'),
    ]

    quantity = models.IntegerField()
    item_note = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=6,decimal_places=2)
    item_discount = models.DecimalField(max_digits=6,decimal_places=2)
    item_total = models.DecimalField(max_digits=6,decimal_places=2)
    item_status = models.CharField(
        max_length=1, choices=ITEM_STATUS_CHOICES, default=ITEM_STATUS_PENDING)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
   

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()




class Admin(models.Model):
    first_name =  models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    