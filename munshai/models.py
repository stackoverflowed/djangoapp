# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from viewflow.models import Process

# Create your models here.

DOC_TYPES = (
    ('ledger', 'LEDGER'),
    ('far', 'FAR')
)


class DocumentUploadProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)
    upload = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    client_id = models.IntegerField(_('Client ID'), primary_key=True)
    # birth_date = models.DateField(_('birthday'))
    client_name = models.CharField(_('Client Name'), max_length=14)
    client_address = models.CharField(_('Address'), max_length=140, default="")
    client_email_address = models.CharField(_('Client Email'), max_length=140, default="")

    # doc_ledger = Document(document_type="LEDGER")

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')
        db_table = 'clients'

    def __str__(self):
        return "{}".format(self.client_name)


class Document(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_('client'))
    document_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # document_id = models.AutoField(primary_key=True)
    document_name = models.CharField(_('Document Name'), max_length=140, default="")
    document_type = models.CharField(_('Document Type'), max_length=140, choices=DOC_TYPES, default='ledger')

    # upload = models.FileField(upload_to='documents/')
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')
        db_table = 'documents'

    def __str__(self):
        return "{}".format(self.document_name)


class ClientDocument(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id', verbose_name=_('client'))
    document = models.ForeignKey(Document, on_delete=models.CASCADE, db_column='document_id',
                                 verbose_name=_('document'))
    # objects = Document.objects.filter(client_id=client)


class Email(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=_('client'))
    email = models.CharField(_('email'), max_length=140, default="")
    document = models.ForeignKey(Document,on_delete=models.CASCADE)
