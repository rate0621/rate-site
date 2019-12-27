from django.urls import path
from . import views

app_name = 'clanbattle'
urlpatterns = [
    path('', views.CbListView.as_view(), name='index'),
    path('update_boss/<int:pk>',   views.BossUpdateView.as_view(),   name='boss_target'),
    path('update_damage/<int:pk>', views.DamageUpdateView.as_view(), name='update_damage'),
]
