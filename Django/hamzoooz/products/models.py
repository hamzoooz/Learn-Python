from django.db import models

# To import Date & Time 
from datetime import datetime

# Create your models here.

class Product(models.Model):

    a =  [
        ('phone', 'phone'),
        ('Computer', 'Computer'),
    ]

    name    = models.CharField(max_length=50)
    content = models.TextField()
    price   = models.DecimalField(max_digits = 5, decimal_places=2)
    # price   = models.DecimalField()
    image   = models.ImageField(upload_to='photos/%y%m%d')
    active  = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=a )
    
    # To Show Product in Browser By Name Can Change To Other Thing 
    def __str__(self):
        return self.name
    
    # To Rename Product in Browser By Name Can Change To Other Thing 
    class Meta:
        verbose_name = 'Product'
        # verbose_name = 'Hamzoooz'

class Test(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    # create = models.DateTimeField(default=datetime.Now)
    create = models.DateTimeField(default=datetime.now )


