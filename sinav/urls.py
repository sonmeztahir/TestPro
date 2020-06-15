from django.urls import path
from .views import list_view, create_view, index_view

app_name = 'sinav'

urlpatterns = [
   path('', index_view, name='index'),
   path('<int:id>/create', create_view, name='create'),
   path('/list', list_view, name='list'),

]
