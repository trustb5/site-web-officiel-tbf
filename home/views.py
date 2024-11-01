from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Mission, Domaine, Offre


def Home(request):
    template_name = 'home/index.html'
    missions = Mission.objects.all()
    context = {
        'missions': missions,
    }
    return render(request, template_name, context)

def Programme(request):
    template_name = 'home/programme.html'
    return render(request, template_name)

def Offres(request):
    template_name = 'home/offres.html'
    offres = Offre.objects.all()
    context = {
        'offres': offres,
    }
    return render(request, template_name, context)



def DomaineAgri(request):
    template_name = 'domaine/agriculture.html'
    domaines = Domaine.objects.all()
    context = {
        'domaines': domaines,
    }
    return render(request, template_name, context)

def DomaineEcon(request):
    template_name = 'domaine/economie.html'
    domaines = Domaine.objects.all()
    context = {
        'domaines': domaines,
    }
    return render(request, template_name, context)

def DomaineEnv(request):
    template_name = 'domaine/environement.html'
    domaines = Domaine.objects.all()
    context = {
        'domaines': domaines,
    }
    return render(request, template_name, context)

def DomaineInfra(request):
    template_name = 'domaine/infrastructure.html'
    domaines = Domaine.objects.all()
    context = {
        'domaines': domaines,
    }
    return render(request, template_name, context)

def DomaineReb(request):
    template_name = 'domaine/reboisement.html'
    domaines = Domaine.objects.all()
    context = {
        'domaines': domaines,
    }
    return render(request, template_name, context)

def DomaineUrgence(request):
    template_name = 'domaine/urgence.html'
    domaines = Domaine.objects.all()
    context = {
        'domaines': domaines,
    }
    return render(request, template_name, context)



def DevisForm(request):
    template_name = 'mission/formulaire-devis.html'
    return render(request, template_name)



def Ecoplus(request):
    template_name = 'ecoplus/index.html'
    return render(request, template_name)

def Dashboard(request):
    template_name = 'admin/admin.html'
    return render(request, template_name)



class addMission(CreateView):
    model = Mission
    fields = ['title', 'image', 'desc']
    success_url = '/showMission/'
    template_name = 'dash/addMission.html'

def showMission(request):
    template_name = 'dash/missions.html'
    missions = Mission.objects.all()
    context = {
        'missions': missions,
    }
    return render(request, template_name, context)

class updateMission(UpdateView):
    model = Mission
    fields = ['title', 'image', 'desc']
    success_url = "/showMission/"
    template_name = 'dash/updateMission.html'



class addDomaine(CreateView):
    model = Domaine
    fields = ['parent', 'title', 'detail', 'image']
    success_url = '/showDomaine/'
    template_name = 'dash/addDomaine.html'

def showDomaine(request):
    template_name = 'dash/domaines.html'
    domaines = Domaine.objects.all()
    context = {
        'domaines': domaines,
    }
    return render(request, template_name, context)



class addOffre(CreateView):
    model = Offre
    fields = ['title', 'detail']
    success_url = '/showOffre/'
    template_name = 'dash/addOffre.html'

def showOffre(request):
    template_name = 'dash/Offres.html'
    offres = Offre.objects.all()
    context = {
        'offres': offres,
    }
    return render(request, template_name, context)



class DashboardView(ListView):
    template_name = 'admin/admin.html'