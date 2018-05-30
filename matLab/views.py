# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .forms import LicenceForm
from .models import Licence
from cgi import escape
from xhtml2pdf import pisa

import datetime
import csv
import StringIO

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
			hostID = licence.hostID
			batiment = licence.batiment
			bureau = licence.bureau
			tel = licence.telephone


			today = datetime.datetime.today()
			date = "{}-{}-{}".format(today.year, today.month, today.day)
                	nomFichier = "matlab-{}-{}_{}-{}".format(release, firstname, name, date)

			# CSV
			activationLabel = "{}-{}-{}-{}".format(firstname, name, release, date)

			csvfile = StringIO.StringIO()
			writer = csv.writer(csvfile)
			writer.writerow([activationLabel, release, hostID, name, firstname, email, bureau, tel, batiment, os])

			# PDF
                        pdfFile =  render_to_pdf(
                                'matLab/licence_details.html',
                                {
                                    'pagesize' : 'A4',
                                    'licence' : licence,
                                })

			# Email à cri@geeps.centralesupelec.fr
			subject = "Activation licence Matlab"
			body = "Demande d\'activation de Matlab {} de {} {} pour le système {}.".format(release, firstname, name, os)
			#sendMail(subject, body, ['cri@geeps.centralesupelec.fr'], nomFichier, csvfile, pdfFile)

			#Email d'acquittement
			subject = "Demande d'activation de la licence Matlab"
			body = "Votre demande d'activation de Matlab {} a bien été prise en compte pour votre système {}.\n\nLe CRI du GeePs".format(release, os)
			sendMailOut(subject, body, [email])
                        
			return redirect('licence_detail', pk=licence.pk)
	else:
		form = LicenceForm()
	return render(request, 'matLab/formulaire.html', {'form':form})

def licence_detail(request, pk):
	licence = get_object_or_404(Licence, pk=pk)
	return render(request, 'matLab/licence_details.html', {'licence':licence})


def sendMail(subject, body, adresses, nameFile, fileCsv, filePdf):
	email = EmailMessage(subject, body, to=adresses)
	email.attach('{}.csv'.format(nameFile), fileCsv.getvalue(), 'text/csv')
        email.attach('{}.pdf'.format(nameFile), filePdf.getvalue(), "application/pdf")
	email.send()


def sendMailOut(subject, body, adresses):
	email = EmailMessage(subject, body, to=adresses)
	email.send()

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context_dict) 
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return result
    return HttpResponse('Nous avons des erreurs')
