from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from jobfair_app import models
# Create your views here.

def index(request):
    #return HttpResponse("JobFair - A place to connect freelancers and employers")
    return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectListView(ListView):
    model = models.Project
    context_object_name = 'project_list'
    template_name = 'project_list.html'

class ProjectDetailView(DetailView):
    model = models.Project
    template_name = 'project_detail.html'
    context_object_name = 'project_detail'
