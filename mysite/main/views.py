from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from social_django.utils import psa
import requests
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.contrib.auth.models import User

from .models import Memories
from .forms import MemoryForm


@psa('social:complete')
def vk_login(request, backend):
    return redirect('main:check_memory')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            print("form is valid")
            memory = form.save(commit=False)
            memory.user = request.user
            memory.date_memorie = datetime.today()
            memory.save()
            return redirect(reverse("main:check_memory"))
        else:
            print(form.errors)
    else:
        form = MemoryForm()
    return render(request, 'main/add_memory.html', {'form': form})

@login_required
def check_memory(request):
    user_memories = Memories.objects.filter(user=request.user)
    user_model = User.objects.get(id=request.user.id)
    user_name = f"{user_model.first_name} {user_model.last_name}"

    social_account = request.user.socialaccount_set.get(provider='vk')
    user_photo_url = social_account.extra_data.get('photo_max_orig')

    context = {
        'memories': user_memories,
        'user_name': user_name,
        'user_photo': user_photo_url,
    }

    print(context)
    
    return render(request, 'main/check_memory.html', context)

@login_required
def edit_memory(request, memory_id):
    memory = get_object_or_404(Memories, id=memory_id)

    if request.method == 'POST':
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            form.save()
            return redirect('main:check_memory')
    else:
        form = MemoryForm(instance=memory)

    return render(request, 'main/edit_memory.html', {'form': form, 'memory': memory})



@login_required
def get_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)

        if form.is_valid():
            print(form.data['memory_name'], '###############################################')
            return HttpResponse('<h1>Form is all right</h1>')
    else:
        form = MemoryForm()
        print('FORM IS BEAD', '###############################################')
    
    return render(request, 'main/add_memory.html', {'form': form})


