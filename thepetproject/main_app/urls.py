from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create', views.ResourceCreate.as_view(), name= 'resources_create' ),
    path('resources/', views.resources_index, name='index'),
]