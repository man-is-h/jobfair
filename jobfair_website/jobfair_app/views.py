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
    user = models.UserProfileInfo
    return render(request,'index.html',{'user':user})

def register(request):

    registered = False
    project_list = models.Project

    if request.method=="POST":

        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            #if 'rating' in request.FILES:
                #profile.rating = request.FILES['rating']
            #if 'description' in request.POST:
            #    profile.description = request.POST['description']
            #if 'role' in request.POST:
            #    profile.role = request.POST['role']
            #if 'project' in request.POST:
            #    profile.project = project_list[request.POST['project']]

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
                return render(request,'index.html',{'user':user})

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
    user_detail = models.UserProfileInfo

class ProjectListView(ListView):
    model = models.Project
    context_object_name = 'project_list'
    template_name = 'project_list.html'


class ProjectDetailView(DetailView):
    model = models.Project
    template_name = 'project_detail.html'
    context_object_name = 'project_detail'

def dashboard(request):
    user_detail = models.UserProfileInfo
    context = {
        'user_detail':user_detail,
    }
    return render(request, 'dashboard.html',context)

def profile(request):
    user_detail = models.UserProfileInfo
    context = {
        'user_detail':user_detail,
    }
    return render(request, 'profile.html',context)

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
