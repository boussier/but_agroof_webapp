from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Tree(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    name = models.CharField('Nom', max_length=250, default='', null=True, blank=True)
    latin_name = models.CharField('Nom latin', max_length=250, default='', null=True, blank=True)
    family = models.CharField('Famille', max_length=250, default='',null=True, blank=True)
    continentality = models.IntegerField('Contiinentalité', null=True, blank=True)
    humidity_a = models.IntegerField('Humidité_a', null=True, blank=True)
    light = models.IntegerField('Lumière', null=True, blank=True)
    ph = models.IntegerField('Ph', null=True, blank=True)
    texture = models.IntegerField('Texture', null=True, blank=True)
    humidity = models.IntegerField('Humidité', null=True, blank=True)
    salinity = models.IntegerField('Salinité', null=True, blank=True)
    organic_material = models.IntegerField('Matière organique', null=True,blank=True)
    name_img = models.CharField('Nom img', max_length=250, default='', null=True,blank=True)

    def __str__(self):
        return '%s' % (self.name)
