from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
# Create your views here.

def index(request):
    #return HttpResponse("JobFair - A place to connect freelancers and employers")
    return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'
