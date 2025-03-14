from django.urls import path
from . import views

app_name = 'vehicules'

urlpatterns = [
    path('', views.home, name='home'),
    path('location/', views.location, name='location'),
    path('profile/', views.profile, name='profile'),
    path('mes-locations/', views.mes_locations, name='mes_locations'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('vehicules/', views.vehicules, name='vehicules'),
    path('vehicules/<int:vehicule_id>/', views.vehicule_detail, name='detail'),
] 