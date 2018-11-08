# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from material.frontend.views import ModelViewSet
from django.shortcuts import get_object_or_404, render, redirect

from munshai.forms import EmailForm
from . import models, forms
from viewflow import flow
from viewflow.flow.views import get_next_task_url



class ClientViewSet(ModelViewSet):
    model = models.Client
    list_display = ('client_id', 'client_name', 'client_email_address', 'client_address')
    list_display_links = ('client_id', 'client_name',)
    list_filterset_fields = ('client_name',)
    # search_fields = ('client_name',)


@login_required
def client_manage_docs(request, client_pk):
    client = get_object_or_404(models.Employee, pk=client_pk)
    form = forms.ChangeSalaryForm(employee=client, data=request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'munshai/manage_docs.html', {

    })

@flow.flow_start_view
def start_upload_workflow(request, **kwargs):
    request.activation.prepare(request.POST or None, user=request.user)
    client_id = request.POST.get("client_id")
    doc_type = request.POST.get("doc_type")
    client = get_object_or_404(models.Client, pk=client_id)
    form = EmailForm(request.POST or None)
    request.activation.done()
    #redirect(get_next_task_url(request, request.activation.process))
    if form.is_valid():
        return redirect(get_next_task_url(request, request.activation.process))

    return render(request, 'munshai/start_workflow.html', {
        'form': form,
        'activation': request.activation
    })