from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create', views.ResourceCreate.as_view(), name= 'resources_create' ),
    path('resources/', views.resources_index, name='index'),
    path('resources/<int:resource_id>', views.resources_detail, name='detail'),
    path('resources/<int:pk>/update/', views.ResourceUpdate.as_view(), name='resources_update'),
    path('resources/<int:pk>/delete/', views.ResourceDelete.as_view(), name='resources_delete'),
    path('resources/<int:resource_id>/add_comment/', views.add_comment, name='add_comment'),
    path('resources/<int:resource_id>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('resources/food', views.resources_food, name='food'),
    path('resources/health', views.resources_health, name='health'),
    path('resources/training', views.resources_training, name='training'),
    path('resources/other', views.resources_other, name='other')

]