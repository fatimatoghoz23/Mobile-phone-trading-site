from django.db import models


# Create your models here.
class Product(models.Model):#نذهب للادمن ونسجل الكلاس ليظهر في قاعدة البيانات

    x=[
        ('photo','photo'),
        ('computer','computer')
    ]
    z=[
        ('i','i'),
        ('p','p')
    ]
    name =models.CharField(max_length=100)
    content=models.TextField()
    ram=models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    category=models.CharField(max_length=100,null=True,choices=x)
    cat=models.CharField(max_length=100,null=True,choices=z)

    def __str__(self):
        return self.name

@property
def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
