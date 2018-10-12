from django.db import models
from django.conf import settings

class TextMessage(models.Model):
	talker= models.CharField(max_length=30,blank=False)
	message= models.CharField(max_length=30,blank=True)

	def _str_(self):
		return self.talker+""+self.message
# Create your models here.
