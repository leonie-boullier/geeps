# -*- coding: utf-8 -*-
from django import forms
from .models import Licence

class LicenceForm(forms.ModelForm):
	class Meta:
		model = Licence
		fields = ('firstname','name', 'email', 'telephone', 'bureau', 'batiment', 'matlabRelease', 'operatingSystem', 'hostID',)
