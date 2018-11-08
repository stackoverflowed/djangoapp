from material import Layout, Row, Fieldset
from viewflow import forms
from django.forms import ModelForm
from .models import Client,Document,Email

class EmailForm(ModelForm):
    class Meta:
        model=Email
        fields = ['client','email','document']