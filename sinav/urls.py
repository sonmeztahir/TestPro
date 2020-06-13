from django.urls import path
from .views import list_view

app_name = 'sinav'

urlpatterns = [
   path('list/', list_view, name='list'),

]
