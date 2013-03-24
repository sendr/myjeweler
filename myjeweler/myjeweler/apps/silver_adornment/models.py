from django.db import models


class Sex(models.Model):

	name = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.name


class SilverRings(models.Model):

	sex = models.ForeignKey(Sex)
	image = models.ImageField(upload_to = 'rings/', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)

	class Meta:
		verbose_name = 'SilverRing'
		verbose_name_plural = 'SilverRings'

	def __unicode__(self):
		return self.name


class TypeEarrings(models.Model):

	name = models.CharField(max_length = 50)

	class Meta:
		verbose_name = 'TypeEarring'
		verbose_name_plural = 'TypeEarrings'

	def __unicode__(self):
		return self.name


class SilverEarrings(models.Model):

	type_earrings = models.ForeignKey(TypeEarrings)
	image = models.FileField(upload_to = 'rings', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)

	class Meta:
		verbose_name = 'SilverEarring'
		verbose_name_plural = 'SilverEarrings'

	def __unicode__(self):
		return self.name


class TypePendants(models.Model):

	name = models.CharField(max_length = 50)

	class Meta:
		verbose_name = 'TypePendant'
		verbose_name_plural = 'TypePendants'

	def __unicode__(self):
		return self.name


class Pendants(models.Model):

	type_pendants = models.OneToOneField(TypePendants)
	image = models.ImageField(upload_to = 'media', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)

	class Meta:
		verbose_name = 'Pendant'
		verbose_name_plural = 'Pendants'

	def __unicode__(self):
		return self.name