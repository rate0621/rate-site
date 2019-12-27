from django.urls import path
from . import views

app_name = 'rate_hp' #django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.index, name='index'),
]
