from django.shortcuts import render, redirect, get_object_or_404, _get_queryset
from .models import QuizModel, QuizAdd
from .classes import karsilastir

def index_view(request):
    themes = QuizModel.objects.all()
    sayi = len(themes)
    return render(request,"sinav/index.html", {'themes': themes, 'sayi':sayi})

def create_view(request, id):
    themes = get_object_or_404(QuizModel, id=id)
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
        return redirect('sinav:index')

    return render(request, 'sinav/save.html', {'themes':themes})


def list_view(request):
    pass