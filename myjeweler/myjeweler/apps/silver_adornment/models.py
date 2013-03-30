from django.db import models
# -*- coding: utf-8 -*-

# class Sex(models.Model):

# 	name = models.CharField(max_length = 20)

# 	def __unicode__(self):
# 		return self.name


class SilverRings(models.Model):

	SEX = (
		(u'Мужское', 'Men'),
		(u'Женское', 'Woman'),
		(u'Унисекс', 'Unisex'),
		)
	image = models.ImageField(upload_to = 'rings', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)
	sex = models.CharField(max_length = 10, choices = SEX)

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
	image = models.FileField(upload_to = 'earrings', blank = True, null = True)
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
	image = models.ImageField(upload_to = 'pendants', blank = True, null = True)
	name = models.CharField(max_length = 50)
	art = models.CharField(max_length = 50)
	weigth = models.CharField(max_length = 50)

	class Meta:
		verbose_name = 'Pendant'
		verbose_name_plural = 'Pendants'

	def __unicode__(self):
		return self.name