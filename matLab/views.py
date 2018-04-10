# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMessage
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

			# Informations
			release = licence.matlabRelease
			firstname = licence.firstname
			name = licence.name
			os = licence.operatingSystem
			email = licence.email

			# Email à cri@geeps.centralesupelec.fr
			subject = "Activation licence Matlab"
			body = "Demande d\'activation de Matlab {} de {} {} pour le système {}.".format(release, firstname, name, os)
			#sendMail(subject, body, ['cri@geeps.centralesupelec.fr'])

			#Email d'acquittement
			subject = "Demande d'activation de la licence Matlab"
			body = "Votre demande d'activation de Matlab {} a bien été prise en compte pour votre système {}".format(release, os)
			#sendMail(subject, body, [email])

			return redirect('licence_detail', pk=licence.pk)

	else:
		form = LicenceForm()
	return render(request, 'matLab/formulaire.html', {'form':form})

def licence_detail(request, pk):
	licence = get_object_or_404(Licence, pk=pk)
	return render(request, 'matLab/licence_details.html', {'licence':licence})


def sendMail(subject, body, adresses):
	email = EmailMessage(subject, body, to=adresses)
	email.send()
