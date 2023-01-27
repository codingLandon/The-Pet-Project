from django.forms import ModelForm
from .models import Comment, User

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['date', 'content']

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name']