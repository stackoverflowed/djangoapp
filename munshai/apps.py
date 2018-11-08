# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class MunshaiAppConfig(ModuleMixin, AppConfig):
    name = 'munshai'
    icon = '<i class="material-icons">settings_applications</i>'
