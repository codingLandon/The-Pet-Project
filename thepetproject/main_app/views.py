from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Resource
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def about(request):
  return render(request, 'about.html')

def home(request):
  return render(request, 'home.html')

@login_required
def resources_index(request):
  resources = Resource.objects.all()
  return render(request, 'resources/index.html', {'resources': resources})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ResourceCreate(CreateView):
  model = Resource
  fields = ['type', 'description', 'location', 'species', ]
  
  def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)


class ResourceUpdate(LoginRequiredMixin, UpdateView):
  model = Resource
  fields = ['type', 'description', 'location', 'species']

class ResourceDelete(LoginRequiredMixin, DeleteView):
  model = Resource
  success_url = '/resources/'

def resources_detail(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    return render(request, 'resources/detail.html', { 'resource': resource })

