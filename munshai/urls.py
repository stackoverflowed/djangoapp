# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.views import generic
from viewflow.flow.viewset import FlowViewSet
from .flows import DocumentUploadFlow
from . import views

from django.conf.urls import url, include
from django.contrib import admin
from material.frontend import urls as frontend_urls

app_name='munshai'
urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='client/'), name="index"),
    #url(r'^docupload/', include(FlowViewSet(DocumentUploadFlow).urls),name='docupload'),
    url(r'^client/', include(views.ClientViewSet().urls)),
]
