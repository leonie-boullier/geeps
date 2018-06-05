# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.

class Licence(models.Model):
	BATIMENTS = (
		('GeePs', 'GeePs'),
		('Breguet', 'Breguet'),
	)
	MATLABRELEASES = (
		('R2017b', 'R2017b'),
		('R2016b', 'R2016b'),
		('R2015b', 'R2015b'),
		('R2014b', 'R2014b'),
		('R2013b', 'R2013b'),
	)

	SYSTEMS = (
		('Windows', 'Windows'),
		('MacOS', 'MacOS'),
		('Linux', 'Linux'),
	)

	name = models.CharField(max_length=50, verbose_name=_("Nom"))
	firstname = models.CharField(max_length=50, verbose_name=_("Prénom"))
	email = models.EmailField(max_length=50, verbose_name=_("Adresse mail"))
	telephone = models.CharField(max_length=10, verbose_name=_("Téléphone"))
	bureau = models.CharField(max_length=200, verbose_name=_("Bureau"))
	batiment = models.CharField(max_length=10, verbose_name=_("Bâtiment"), choices=BATIMENTS, default="GeePs")
	matlabRelease = models.CharField(max_length=10, verbose_name=_("Version de MatLab"), choices=MATLABRELEASES, default="R2017b")
	operatingSystem = models.CharField(max_length=10 , verbose_name=_("Système"), choices=SYSTEMS, default="Windows")
	hostID = models.CharField(max_length=17)


	def __str__(self):
		return self.firstname+' '+self.name
