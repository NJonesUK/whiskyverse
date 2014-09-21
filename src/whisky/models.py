from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class Region(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.name
	
class Whisky(models.Model):
	name = models.CharField(max_length=255)
	strength = models.FloatField(blank=True, null=True)
	age = models.IntegerField(blank=True, null=True)
	cask_type = models.CharField(max_length=255)
	bottled_in = models.IntegerField(blank=True, null=True)
	size = models.IntegerField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class Distillery(models.Model):
	name = models.CharField(max_length=255)
	region = models.ForeignKey(Region, blank=True, null=True)
	country = models.ForeignKey(Country, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return self.name

class DistilleryWhisky(models.Model):
	distillery = models.ForeignKey(Distillery)
	whisky = models.ForeignKey(Whisky)

class Brand(models.Model):
	name = models.CharField(max_length=255)
	country = models.ForeignKey(Country)
	description = models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return self.name
class BrandWhisky(models.Model):
	brand = models.ForeignKey(Brand)
	whisky = models.ForeignKey(Whisky)

class Type(models.Model):
	pass

class District(models.Model):
	pass

class UserScore(models.Model):
	user = models.ForeignKey(User)
	whisky = models.ForeignKey(Whisky)
	score = models.IntegerField()
	notes = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.user + ": " + self.whisky

	class Meta():
		unique_together = ("user", "whisky")

