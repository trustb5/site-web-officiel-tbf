from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Mission


def Home(request):
    template_name = 'home/index.html'
    return render(request, template_name)

def Programme(request):
    template_name = 'home/programme.html'
    return render(request, template_name)

def Offres(request):
    template_name = 'home/offres.html'
    return render(request, template_name)



def DomaineAgri(request):
    template_name = 'domaine/agriculture.html'
    return render(request, template_name)

def DomaineEcon(request):
    template_name = 'domaine/economie.html'
    return render(request, template_name)

def DomaineEnv(request):
    template_name = 'domaine/environement.html'
    return render(request, template_name)

def DomaineInfra(request):
    template_name = 'domaine/infrastructure.html'
    return render(request, template_name)

def DomaineReb(request):
    template_name = 'domaine/reboisement.html'
    return render(request, template_name)

def DomaineUrgence(request):
    template_name = 'domaine/urgence.html'
    return render(request, template_name)



def MissionSante(request):
    template_name = 'mission/santepublic.html'
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


class DashboardView(ListView):
    template_name = 'admin/admin.html'