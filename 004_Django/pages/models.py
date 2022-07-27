from django.db import models

class Login(models.Model):

    username = models.CharField(max_length=50 )
    password = models.CharField(max_length=50 )

    def __str__(self):
        return self.username

# class Pages(models.Model):
#     pass

# # Create your models here.
# class Female(models.Model):
#     name_female = models.CharField(max_length=50, null=True)
#     def __str__(self):
#         return self.name_female
    
# class Male(models.Model):
#     name_male = models.CharField(max_length=50, null=True)
#     girls = models.OneToOneField(Female, on_delete=models.CASCADE )
#     # girls = models.OneToOneField(Female, on_delete=models.CASCADE(collector, field, sub_objs, using))
#     # girls = models.OneToOneField(Female, on_delete=models.PROTECT(collector, field, sub_objs, using)
#     def __str__(self):
#         return self.name_male
# class Products(models.Model):
#     title = models.CharField(max_length=50, null=True)
    
#     def __str__(self):
#         return self.title
    
# class User(models.Model):
#     name = models.CharField(max_length=50, null=True)
#     product = models.ForeignKey(Products, on_delete=models.CASCADE )
    
#     def __str__(self):
#         return self.name

# class Vedio(models.Model):
#     title = models.CharField(max_length=50, null=True)
    
#     def __str__(self):
#         return self.title
    
# class User_name(models.Model):
#     name = models.CharField(max_length=50, null=True)
#     watch = models.ManyToManyField(Vedio, null=True )
    
#     def __str__(self):
#         return self.name