from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    create_time = models.DateTimeField(_("created time") ,auto_now_add=True)
    modified_time = models.DateTimeField(_("modified time") ,auto_now=True)


    class meta:
        abstract = True

        