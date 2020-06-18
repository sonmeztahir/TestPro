from django.shortcuts import render, redirect, get_object_or_404
from .models import QuizModel, QuizAdd
from .classes import karsilastir
from django.contrib import messages

def index_view(request):
    themes = QuizModel.objects.all()
    sayi = len(themes)
    return render(request, "sinav/index.html", {'themes': themes, 'sayi': sayi})


def create_view(request, id):
    themes = get_object_or_404(QuizModel, id=id)
    context = QuizAdd.objects.extra(where=["number='{}'".format(request.user.numara), "quiz_name='{}'".format(themes.quiz_name)])
    if context:
        messages.error(request, 'Bu Sınavı Daha Önce Çözdünüz!!!')
        return redirect('sinav:index')

    if not request.user.is_authenticated:
        messages.info(request, 'Testleri çözmek için giriş yapmalısınız!')
        return redirect('sinav:index')

    if request.method == 'POST':
        department = request.POST.get('Sınıfı')
        name = request.POST.get('Adı')
        number = request.POST.get('Numarası')
        answer_key = request.POST.get('Cevap Anahtarı')
        quiz_name = request.POST.get('Sınav Adı')


        cevap = ''
        for i in range(1, len(request.POST.get('Cevap Anahtarı')) + 1):
            cevap = "{}{}".format(cevap, request.POST.get('cevap{}'.format(i), None))
        answer = cevap

        quiz_result = karsilastir(answer, answer_key)

        kaydet = QuizAdd(department=department, name=name, number=number, answer=answer, answer_key=answer_key, quiz_name=quiz_name, quiz_result=quiz_result)
        kaydet.save()
        return redirect('sinav:list')

    return render(request, 'sinav/save.html', {'themes': themes})


def list_view(request):
    context = QuizAdd.objects.extra(where=["number={}".format(request.user.numara)])
    return render (request, 'sinav/liste.html', {'context':context})
