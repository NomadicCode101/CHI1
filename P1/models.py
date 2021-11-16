from django.db import models

# Create your models here.



# class Customer(models.Model):
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name



class Org(models.Model):
	name = models.CharField(max_length=100,null= True)
	Otype = models.CharField(max_length=100, null= True)
	Csize = models.IntegerField(null= True)
	Place = models.CharField(max_length=255, null = True)

	def __str__(self):
		return self.name

