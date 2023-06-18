from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from music_app.models import MusicFile

    

def indexview(request):
    return render(request, 'music_app/index.html')

@login_required
def upload_music_file(request):
    if request.method == 'POST':
        file = request.FILES.get('music_file')
        access = request.POST.get('access')
        allowed_emails = request.POST.get('allowed_emails')
        music_file = MusicFile.objects.create(user=request.user, file=file, access=access, allowed_emails=allowed_emails)
        return redirect('home')
    return render(request, 'music_app/upload.html')


class HomeView(View):
    def get(self, request):
        music_files = MusicFile.objects.filter(access=MusicFile.PUBLIC) | \
                      MusicFile.objects.filter(user=request.user) | \
                      MusicFile.objects.filter(access=MusicFile.PROTECTED, allowed_emails__contains=request.user.email)
        context = {'music_files': music_files}
        return render(request, 'music_app/home.html', context)

# def home(request):
#    return render(request, 'home.html')

class Registration(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'music_app/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'music_app/register.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('index')