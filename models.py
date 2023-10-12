from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Create your models here.

class Customer(models.Model):
	
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name
	
	
class Product(models.Model):#نذهب للادمن ونسجل الكلاس ليظهر في قاعدة البيانات

    x=[
        ('photo','photo'),
        ('computer','computer'),
	      ('accessory','accessory')
	      
    ]
    
    z=[
        ('i','i'),
        ('p','p')
	      
    ]
    price2=models.IntegerField(null=True, blank=True)

    name =models.CharField(max_length=100)
    content=models.TextField()
    ram=models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=0)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    category=models.CharField(max_length=100,null=True,choices=x)
    storage = models.DecimalField(max_digits=6,decimal_places=0,null=True, blank=True)
    index=models.CharField(max_length=100,null=True,choices=z)
    digital = models.BooleanField(default=False,null=True, blank=True)

    def __str__(self):
      return self.name
    @property
    def imageURL(self):
					try:
						url = self.image.url
					except:
						url = ''
					return url
    
	   


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	
	@property
	def shipping(self):#للشحن
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:#  اذا المنتج رقمي يساوي خطأ
				shipping = True#العنصر يحتاج الى شحن
		return shipping

	@property
	def get_cart_total(self):#حساب اجمالي سعر الطلبيات
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):#اجمالي عدد الطلبيات
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):#يقوم بحساب الطلبية لعنصر  
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address    
class review(models.Model):
			text= models.TextField(max_length=300)
			customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
			product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
			created=models.DateTimeField(auto_now_add=True)
			
			def __str__(self):
      				return self.text