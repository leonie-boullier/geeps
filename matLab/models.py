# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

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

	name = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	telephone = models.CharField(max_length=10)
	bureau = models.CharField(max_length=200)
	batiment = models.CharField(max_length=10, choices=BATIMENTS, default="GeePs")
	matlabRelease = models.CharField(max_length=10, choices=MATLABRELEASES, default="R2017b")
	operatingSystem = models.CharField(max_length=10 , choices=SYSTEMS, default="Windows")
	hostID = models.IntegerField()

	def __str__(self):
		return self.firstname+' '+self.name
