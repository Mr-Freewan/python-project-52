from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name=_('Name'),
                            unique=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Creation date'))

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    def __str__(self):
        return self.name
