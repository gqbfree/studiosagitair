from django.db import models
from django import forms
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from filer.models import *
from image_cropping import ImageRatioField, ImageCropField

import json
import sys
#import string
import re



# Create your models here.
'''
class Gallery(models.Model):
    #titolo = models.CharField(max_length=200,  null=True, blank=True)
    #post = models.ForeignKey(Post)
    #didascalia = models.TextField(null=True, blank=True)
    #image = models.ImageField(upload_to='uploaded_galleria')
    image_field = FilerImageField(related_name="test_gallery")

class Immagini(models.Model):
    titolo = models.CharField(max_length=100)
    image = models.ForeignKey(Gallery)
    cropping = ImageRatioField('image__image_field', '700x500')
	    
    class Meta:
        verbose_name_plural = "Immagini"


class Prova(models.Model):
    titolo = models.CharField(max_length=100)
    proof = models.ManyToManyField(Immagini)

    def __unicode__(self):
        return self.titolo

'''
class Categorie(models.Model):
    titolo = models.CharField(max_length=100)

    def __unicode__(self):
        return self.titolo

class Galleria(models.Model):
       image_field = FilerImageField(related_name="immagini_gallery")

       class Meta:
        verbose_name_plural = "Galleria importa immagini da Filer"

class Immagini(models.Model):
    titolo = models.CharField("Titolo del Progetto:", max_length=100)
    image = models.ForeignKey(Galleria, null=True, blank=True, verbose_name="Seleziona Immagine")
    didascalia = models.TextField(null=True, blank=True)
    cropping = ImageRatioField('image__image_field', '500x480')
    slidepage = ImageRatioField('image__image_field', '870x480')
    #croppingthumb = ImageRatioField('image__image_field', '119x67')
    croppingthumb = ImageRatioField('image__image_field', '595x335')
    croppingslide = ImageRatioField('image__image_field', '1140x487')
    croppingcarousel = ImageRatioField('image__image_field', '198x132')
    croppingrender = ImageRatioField('image__image_field', '700x500')
    designthumb = ImageRatioField('image__image_field', '500x469')
    designbig = ImageRatioField('image__image_field', '1200x800')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Immagini"


class Planimetria(models.Model):
    titolo = models.CharField("Titolo del Progetto:", max_length=100)
    image = models.ForeignKey(Galleria, null=True, blank=True, verbose_name="Seleziona Immagine")
    didascalia = models.TextField(null=True, blank=True)
    cropping = ImageRatioField('image__image_field', '535x656')
    croppingthumb = ImageRatioField('image__image_field', '1070x1312')
    croppingslide = ImageRatioField('image__image_field', '1070x1312', free_crop=True)
    croppingcarousel = ImageRatioField('image__image_field', '1312x1070', free_crop=True)
    croppingrender = ImageRatioField('image__image_field', '1070x1070', free_crop=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Planimetrie"

class Video(models.Model):
    titolo = models.CharField("Titolo del Video:", max_length=100, null=True, blank=True)
    youtubeurl = models.CharField("Indirizzo url youtube:", max_length=100, null=True, blank=True)
    embedded = models.TextField("Codice Embedded YouTube", null=True, blank=True)
    thumb = models.ImageField(upload_to='uploaded_thum_youtube', null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)

    def idyoutube(self):
        youid = re.findall(r'embed/(.*?)rel=', self.embedded)[0][:-1]
        return youid

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Video"

IMPAGINAZIONE_CHOICES = (
    ('0', 'VERTICALE'),
    ('1', 'ORIZZONTALE'),
                )

class Post(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_eng = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    categoria = models.ManyToManyField(Categorie, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_eng = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ForeignKey(Galleria, null=True, blank=True, verbose_name="Seleziona Immagine")
    cropping = ImageRatioField('image__image_field', '500x281')
    croppingdesign = ImageRatioField('image__image_field', '500x469')
    impaginazione = models.CharField(choices=IMPAGINAZIONE_CHOICES, max_length=200, null=True, blank=True)
    planimetria = models.ForeignKey(Planimetria, null=True, blank=True)
    croppingplan = ImageRatioField('planimetria__image_field', '700x500')
    video = models.ManyToManyField(Video, null=True, blank=True)
    galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo


'''
class Design(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    categoria = models.ManyToManyField(Categorie, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ForeignKey(Galleria, null=True, blank=True, verbose_name="Seleziona Immagine")
    croppingthumb = ImageRatioField('image__image_field', '500x469', free_crop=True)
    centralethumb = ImageRatioField('image__image_field', '500x469')
    centralebig = ImageRatioField('image__image_field', '1200x1126')
    #video = models.ManyToManyField(Video, null=True, blank=True)
    galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    #pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = "Design"

    def __unicode__(self):
        return self.titolo

'''







