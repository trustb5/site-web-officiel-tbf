from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home, name='home'),
    path('programme', views.Programme, name='programme'),
    path('offres', views.Offres, name='offres'),
    path('ecoplus', views.Ecoplus, name='ecoplus'),
    path('dashboard/', views.Dashboard, name='dash'),

    path('addMission/', views.addMission.as_view(), name='addMission'),
    path('showMission/', views.showMission, name='showMission'),
]