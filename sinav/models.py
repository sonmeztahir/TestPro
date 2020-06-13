from django.db import models

class QuizModel(models.Model):
    quiz_name = models.CharField(max_length=100, verbose_name='Sınav Adı')
    ansver_key = models.CharField(max_length=100, verbose_name='Cevap Anahtarı')
    quiz_file = models.FileField(verbose_name='Sınav Dosyası')
    publishing_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi')

    def __str__(self):
        return self.quiz_name