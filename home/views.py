from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Mission

class GeeksCreate(CreateView):
    model = Mission
    fields = ['title', 'description']

class GeeksList(ListView):

    # specify the model for list view
    model = Mission

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

def Home(request):
    template_name = 'home/index.html'
    return render(request, template_name)

