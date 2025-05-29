from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_or_signup, name='login'),  
    path('signup/', views.login_or_signup, name='signup'),  
    path('recipes/', views.recipes, name="recipes"),
    path('add_recipe/', views.add_recipe, name="add_recipe"),
    path('edit_recipe/', views.edit_recipe, name="edit_recipe"),
    path('view_recipe/', views.view_recipe, name="view_recipe"),

    path('sign_up/', views.sign_up, name="sign_up"),
    path('log_in/', views.log_in, name="log_in"),
    path('login/sign_up/', views.sign_up, name="sign_up"),
    path('login/log_in/', views.log_in, name="log_in"),
    path('signup/sign_up/', views.sign_up, name="sign_up"),
    path('signup/log_in/', views.log_in, name="log_in"),

    path('add_recipe/create_recipe/', views.create_recipe, name="create_recipe"),
    path('get_recipes/', views.get_recipes, name='get_recipes'),
    path('recipes/get_recipes/', views.get_recipes, name='get_recipes'),
]   
