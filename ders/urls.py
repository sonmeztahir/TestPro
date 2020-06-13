from django.urls import path
from .views import list_view, detail_view

app_name = 'ders'

urlpatterns = [
   path('', list_view, name='index'),
   path('<int:id>/detail', detail_view, name='detail'),
]
