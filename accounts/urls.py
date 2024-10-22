from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('dash/', views.Dash, name='dash'),
]