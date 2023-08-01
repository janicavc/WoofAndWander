from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
	
urlpatterns = [
	path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('places/', views.places_index, name='index'), 
    # path('profile/', views.user_profile, name='profile'), 
    path('profiles/<int:profile_id>', views.profile_details, name='profile_details'), 
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'), 
]