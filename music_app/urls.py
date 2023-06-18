from django.urls import path
from music_app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from music_app.views import upload_music_file, indexview

urlpatterns = [
    path('', indexview, name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('register/', views.Registration.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='music_app/login.html', authentication_form=LoginForm), name='login'),
    path('upload/', upload_music_file, name='upload'),
    path('logout/', views.user_logout, name='logout'),
]