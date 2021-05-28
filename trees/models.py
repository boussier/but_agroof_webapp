from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Tree(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    name = models.CharField('Nom', max_length=250, default='', null=True, blank=True)
    latin_name = models.CharField('Nom latin', max_length=250, default='', null=True, blank=True)
    family = models.CharField('Famille', max_length=250, default='',null=True, blank=True)
    continentality_min = models.IntegerField('Contiinentalité min', null=True, blank=True)
    continentality_max = models.IntegerField('Contiinentalité max', null=True, blank=True)
    humidity_a_min = models.IntegerField('Humidité_a min', null=True, blank=True)
    humidity_a_max = models.IntegerField('Humidité_a max', null=True, blank=True)
    light_min = models.IntegerField('Lumière min', null=True, blank=True)
    light_max = models.IntegerField('Lumière max', null=True, blank=True)
    ph_min = models.IntegerField('Ph min', null=True, blank=True)
    ph_max = models.IntegerField('Ph max', null=True, blank=True)
    texture_min = models.IntegerField('Texture min', null=True, blank=True)
    texture_max = models.IntegerField('Texture max', null=True, blank=True)    
    humidity_min = models.IntegerField('Humidité min', null=True, blank=True)
    humidity_max = models.IntegerField('Humidité max', null=True, blank=True)
    salinity_min = models.IntegerField('Salinité min', null=True, blank=True)
    salinity_max = models.IntegerField('Salinité max', null=True, blank=True)
    organic_material_min = models.IntegerField('Matière organique min', null=True,blank=True)
    organic_material_max = models.IntegerField('Matière organique max', null=True,blank=True)
    temperature_min = models.IntegerField('Température min', null=True, blank=True)
    temperature_max = models.IntegerField('Température max', null=True, blank=True)
    nutrient_min = models.IntegerField('Nutriment min', null=True, blank=True)
    nutrient_max = models.IntegerField('Nutriment max', null=True, blank=True)
    name_img = models.CharField('Nom img', max_length=250, default='', null=True,blank=True)

    def __str__(self):
        return '%s' % (self.name)
