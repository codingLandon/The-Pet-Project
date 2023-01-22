from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create', views.ResourceCreate.as_view(), name= 'resources_create' ),
    path('resources/', views.resources_index, name='index'),
    path('resources/<int:resource_id>', views.resources_detail, name='detail'),
    path('resources/<int:pk>/update/', views.ResourceUpdate.as_view(), name='resources_update'),
    path('resources/<int:pk>/delete/', views.ResourceDelete.as_view(), name='resources_delete'),
    path('resources/<int:resource_id>/add_comment/', views.add_comment, name='add_comment'),

]