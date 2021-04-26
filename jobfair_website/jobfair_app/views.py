from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (View, TemplateView,
                                    ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView)
from jobfair_app import models
from jobfair_app.forms import UserForm, UserProfileInfoForm

from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    #return HttpResponse("JobFair - A place to connect freelancers and employers")
    return render(request,'index.html')

def register(request):

    registered = False
    project_list = models.Project

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'rating' in request.FILES:
                profile.rating = request.FILES['rating']
            if 'description' in request.FILES:
                profile.description = request.FILES['description']
            if 'role' in request.FILES:
                profile.role = request.FILES['role']
            if 'project' in request.FILES:
                profile.project = request.FILES['project']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request, 'registration.html',
                    {'user_form':user_form,
                        'profile_form':profile_form,
                        'registered':registered,
                        'project_list':project_list,})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Someone Tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            wrong_credential = True
            return render(request, 'login.html', {'wrong_credential':wrong_credential,})

    else:
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectListView(ListView):
    model = models.Project
    context_object_name = 'project_list'
    template_name = 'project_list.html'

class FreelancerListView(ListView):
    model = models.Freelancer
    context_object_name = 'freelancer_list'
    template_name = 'freelancer_list.html'

class ProjectDetailView(DetailView):
    model = models.Project
    template_name = 'project_detail.html'
    context_object_name = 'project_detail'

class FreelancerDetailView(DetailView):
    model = models.Freelancer
    template_name = 'freelancer_detail.html'
    context_object_name = 'freelancer_detail'

class ProjectCreateView(CreateView):
    model = models.Project
    fields = ('name', 'description', 'stipend','upvote','downvote','skills')
    template_name = 'project_form.html'

class ProjectUpdateView(UpdateView):
    model = models.Project
    fields = ('name','description','stipend','upvote','downvote','skills')
    template_name = 'project_form.html'

class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy('jobfair_app:project_list')
    template_name = 'project_confirm_delete.html'
