from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class ThemeModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    content = RichTextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ders:detail', kwargs={'id': self.id})