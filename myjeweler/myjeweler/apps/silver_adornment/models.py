from django.db import models


class Sex(models.Model):

	name = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.name


class SilverRings(models.Model):

	sex = models.OneToOneField(Sex)
	image = models.FileField(upload_to = 'rings', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name


class TypeEarrings(models.Model):

	name = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name


class SilverEarrings(models.Model):

	type_earrings = models.OneToOneField(TypeEarrings)
	image = models.FileField(upload_to = 'rings', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name


class TypePendants(models.Model):

	name = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name


class Pendants(models.Model):

	type_pendants = models.OneToOneField(TypePendants)
	image = models.FileField(upload_to = 'rings', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name