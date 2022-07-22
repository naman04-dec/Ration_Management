from django.db import models


# Create your models here.
class govRation(models.Model):
    shop_name=models.CharField(max_length=40)
    aadhar_num=models.IntegerField(unique = True)
    sugar_quant=models.IntegerField()
    wheat_quant=models.IntegerField()
    rice_quant=models.IntegerField()
    date=models.DateField();
