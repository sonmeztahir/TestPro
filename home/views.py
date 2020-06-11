from django.shortcuts import render, redirect
from .models import Home_Static, Home_Post

def index_view(request):
	home_static = Home_Static.objects.all()
	home_post = Home_Post.objects.all()
	return render(request, "index.html", {'home_static': home_static, 'home_post':home_post})