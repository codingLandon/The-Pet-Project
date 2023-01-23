from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Resource, Comment
from .forms import CommentForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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
    comment_form = CommentForm()
    return render(request, 'resources/detail.html', {
    'resource': resource, 'comment_form': comment_form
  })

@login_required
def add_comment(request, resource_id):
    form = CommentForm(request.POST)
  # validate the form
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.resource_id = resource_id
        new_comment.user = request.user
        new_comment.save()
    return redirect('detail', resource_id=resource_id)

@login_required
def delete_comment(request, comment_id, resource_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(request, 'detail', resource_id=resource_id)
