from django.db import models

class Home_Static(models.Model):
	title = models.CharField(max_length=50, verbose_name='Başlık')
	content = models.TextField(verbose_name='içerik')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']


class Home_Post(models.Model):
	image = models.ImageField(null=True, blank=True, verbose_name='Resim')
	title = models.CharField(max_length=100, verbose_name='Başlık')
	content = models.TextField(verbose_name='İçerik')
	publishing_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-publishing_date']