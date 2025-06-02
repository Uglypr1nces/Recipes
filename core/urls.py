from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_or_signup, name='login'),  
    path('signup/', views.login_or_signup, name='signup'),  
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_sight/', views.add_sight, name="add_sight"),
    path('edit_sight/', views.edit_sight, name="edit_sight"),
    path('view_sight/', views.view_sight, name="view_sight"),

    path('sign_up/', views.sign_up, name="sign_up"),
    path('log_in/', views.log_in, name="log_in"),
    path('login/sign_up/', views.sign_up, name="sign_up"),
    path('login/log_in/', views.log_in, name="log_in"),
    path('signup/sign_up/', views.sign_up, name="sign_up"),
    path('signup/log_in/', views.log_in, name="log_in"),

    path('dashboard/get_sights/', views.get_sights, name='get_sights'),
    path('dashboard/delete_sight/', views.delete_sight, name='delete_sight'),

    path('add_sight/import_sight/', views.import_sight, name="import_sight"),
    path('view_sight/get_specific_sight/', views.get_specific_sight, name='get_specific_sight'),
    path('edit_sight/change_sight/', views.change_sight, name='change_sight'),    
]   
