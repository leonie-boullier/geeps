# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LicenceForm

# Create your views here.

def formulaire(request):
	form = LicenceForm()
	return render(request, 'matLab/formulaire.html', {'form':form})
