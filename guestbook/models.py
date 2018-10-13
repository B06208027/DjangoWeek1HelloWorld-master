from django.db import models
from django.conf import settings

class TextMessage(models.Model):
	talker= models.CharField(max_length=30,blank=False)
	message= models.CharField(max_length=30,blank=True)
	date_time = models.DateTimeField()

	def _str_(self):
		return self.talker+""+self.message+""+self.date_time
# Create your models here.
