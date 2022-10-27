from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

#once your model is done, go to the views.py app where you want this info to be share with. 
#This case, jump into the views.py inside the pos file

# Create your models here.
class Product(models.Model){
    product_name=models.CharField(max_length=200, unique=True)
    
}


