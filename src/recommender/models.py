from django.db import models

from whisky.models import Distillery

# Create your models here.

class DistilleryProfile(models.Model):
	distillery = models.ForeignKey(Distillery)
	body = models.IntegerField()
	sweetness = models.IntegerField()
	smokey = models.IntegerField()
	medicinal = models.IntegerField()
	tobacco = models.IntegerField()
	honey = models.IntegerField()
	spicy = models.IntegerField()
	winey = models.IntegerField()
	nutty = models.IntegerField()
	malty = models.IntegerField()
	fruity = models.IntegerField()
	floral = models.IntegerField()
	postcode = models.CharField(max_length=15)
	latitude = models.IntegerField()
	longitude = models.IntegerField()

	def __unicode__(self):
		return self.distillery.name