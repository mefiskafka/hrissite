from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.
class Contacts(models.Model):
	member_name=models.CharField(max_length=200)
	position=models.CharField(max_length=200)
	phone_number=models.CharField(max_length=15, blank=True)
	e_mail=models.EmailField(max_length=200,  blank=True)
	address=models.CharField(max_length=200,  blank=True)
	
	def __unicode__(self):   # Python 3: def __str__(self):
		return self.member_name
			
class ContactsPlugin(CMSPlugin):
	title=models.CharField(max_length=200, default='implementers')
	
