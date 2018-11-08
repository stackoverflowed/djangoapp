from django.db import models

class DocumentQuerySet(models.QuerySet):
    def set(self,**kwargs):
        self.filter()