from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name= 'home'),
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('search/', views.search_results, name='search_results')
]