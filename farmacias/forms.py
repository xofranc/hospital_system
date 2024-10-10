# farmacias/forms.py

from django import forms

class EnviarRecetaForm(forms.Form):
    farmacia = forms.CharField(max_length=100)
    receta_id = forms.IntegerField(widget=forms.HiddenInput())
