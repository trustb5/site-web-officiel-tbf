from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Mission, Domaine, Offre, Contact


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

def About(request):
    template_name = 'home/about.html'
    return render(request, template_name)

def Offres(request):
    template_name = 'home/offres.html'
    offres = Offre.objects.all()
    context = {
        'offres': offres,
    }
    return render(request, template_name, context)


def error_404(request, exception):
    return render(request, 'error_404.html', status=404)
 
def error_500(request):
    return render(request, 'error_505.html', status=500)
 
def search(request):
    return render(request, 'home/search.html')



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

class updateDomaine(UpdateView):
    model = Domaine
    fields = ['parent', 'title', 'detail', 'image']
    success_url = "/showDomaine/"
    template_name = 'dash/updateDomaine.html'

def deleteDomaine(request, pk):
    obj = Domaine.objects.get(id = pk)
    template_name = 'dash/domains.html'
    if request.method == "POST":
        obj.delete()
        return redirect("home:showDomaine")
    return render(request, template_name)



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



class addContact(CreateView):
    model = Contact
    fields = ['name', 'email', 'message']
    success_url = '/'
    template_name = 'home/index.html'

def showContact(request):
    template_name = 'dash/contacts.html'
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, template_name, context)



class DashboardView(ListView):
    template_name = 'admin/admin.html'