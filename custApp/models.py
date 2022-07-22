from django.db import models

# Create your models here.
class custRation(models.Model):
    customer_name=models.CharField(max_length=40)
    aadhar_num=models.IntegerField()
    sugar_quant=models.IntegerField()
    wheat_quant=models.IntegerField()
    rice_quant=models.IntegerField()
    date=models.DateTimeField(unique = True);
