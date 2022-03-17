from django.db import models

# Create your models here.
class Contact_Us(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, db_index= True)
    message = models.TextField(default=False)
    date = models.DateTimeField(auto_now_add=True)