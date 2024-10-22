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

def Ecoplus(request):
    template_name = 'home/ecoplus.html'
    return render(request, template_name)

def Dashboard(request):
    template_name = 'admin/admin.html'
    return render(request, template_name)


class addMission(CreateView):
    model = Mission
    template_name = 'dash/missionForm.html'
    success_url = '/showMission/'
    fields = ['title', 'image', 'desc']

def showMission(request):
    template_name = 'dash/missions.html'
    missions = Mission.objects.all()
    context = {
        'missions': missions,
    }
    return render(request, template_name, context)


class DashboardView(ListView):
    template_name = 'admin/admin.html'

class GeeksDetailView(DetailView):
    # specify the model to use
    model = Mission

class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = Mission

    # specify the fields
    fields = [
        "title",
        "description"
    ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"

class GeeksDeleteView(DeleteView):
    # specify the model you want to use
    model = Mission
    
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"