from django.shortcuts import render, get_object_or_404
from .models import ThemeModel

def list_view(request):
    themes = ThemeModel.objects.all()
    return render(request,"ders/index.html", {'themes': themes})

def detail_view(request, id):
    themes = get_object_or_404(ThemeModel, id=id)
    context = {
        'themes': themes
    }
    return render(request, "ders/detail.html", context)