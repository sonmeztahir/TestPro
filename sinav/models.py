from django.db import models
from django.urls import reverse

class QuizModel(models.Model):
    quiz_name = models.CharField(max_length=100, verbose_name='Sınav Adı')
    answer_key = models.CharField(max_length=100, verbose_name='Cevap Anahtarı')
    quiz_file = models.FileField(verbose_name='Sınav Dosyası')
    publishing_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi')

    def __str__(self):
        return self.answer_key

    def get_absolute_url(self):
        return reverse('sinav:create', kwargs={'id':self.id})

class QuizAdd(models.Model):
    department = models.CharField(max_length=3, verbose_name='Sınıf')
    name = models.CharField(max_length=100, verbose_name='İsim')
    number = models.IntegerField(verbose_name='Numara')
    answer = models.CharField(max_length=50, verbose_name='Cevap')
    answer_key = models.CharField(max_length=100, verbose_name='Cevap Anahtarı')
    quiz_name = models.CharField(max_length=100, verbose_name='Sınavın Adı')
    quiz_result = models.IntegerField(blank=True, null=True, verbose_name='Aldığı Puan')
    publishing_date = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')


    def __str__(self):
        return self.name