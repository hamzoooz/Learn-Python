from django.db import models

# Create Your Models

class SingUp(models.Model ):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestap = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

# def __unicode__(self):
#     return self
def __str__(self):
    return self