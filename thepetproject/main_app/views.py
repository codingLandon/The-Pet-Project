from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Resource
# Create your views here.
def about(request):
  return render(request, 'about.html')

def home(request):
  return render(request, 'home.html')

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

def resources_detail(request):
  pass