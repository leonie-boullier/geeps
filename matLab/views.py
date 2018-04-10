# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .forms import LicenceForm
from .models import Licence

# Create your views here.

def formulaire(request):
	if request.method == "POST":
		form = LicenceForm(request.POST)
		if form.is_valid():
			licence = form.save(commit=False)
			licence.save()
			return redirect('licence_detail', pk=licence.pk)
	else:
		form = LicenceForm()
	return render(request, 'matLab/formulaire.html', {'form':form})

def licence_detail(request, pk):
	licence = get_object_or_404(Licence, pk=pk)
	return render(request, 'matLab/licence_details.html', {'licence':licence})
