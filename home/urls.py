from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home, name='home'),
    path('programme', views.Programme, name='programme'),
    path('offres', views.Offres, name='offres'),

    path('domaine/agriculture', views.DomaineAgri, name='agri'),
    path('domaine/economie', views.DomaineEcon, name='econ'),
    path('domaine/environement', views.DomaineEnv, name='env'),
    path('domaine/infrastructure', views.DomaineInfra, name='infra'),
    path('domaine/reboisement', views.DomaineReb, name='reb'),
    path('domaine/urgence', views.DomaineUrgence, name='urgence'),

    path('mission/formulaire-devis', views.DevisForm, name='devis-form'),
    
    path('ecoplus', views.Ecoplus, name='ecoplus'),
    path('dashboard/', views.Dashboard, name='dash'),

    path('addMission/', views.addMission.as_view(), name='addMission'),
    path('showMission/', views.showMission, name='showMission'),
    path('updateMission/<pk>', views.updateMission.as_view(), name='updateMission'),

    path('addDomaine/', views.addDomaine.as_view(), name='addDomaine'),
    path('showDomaine/', views.showDomaine, name='showDomaine'),

    path('addOffre/', views.addOffre.as_view(), name='addOffre'),
    path('showOffre/', views.showOffre, name='showOffre'),
]