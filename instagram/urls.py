from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search_results, name='search_results')
]
