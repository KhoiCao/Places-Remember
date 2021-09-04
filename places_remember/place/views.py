from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Memory

def place_home(request):
    return render(request, 'place/home.html')


@login_required
def place_list(request):
    user_memories = Memory.objects.filter(owner=request.user)
    context = {
        'avatar_url' : request.user.social_auth.get().extra_data['avatar_url'],
        'memories' : user_memories
    }
    return render(request, 'place/list.html', context)


@login_required
def place_add(request):
    context = {
        'avatar_url' : request.user.social_auth.get().extra_data['avatar_url']
    }
    if request.method == 'POST':
        memory_name = request.POST['memory_name']
        comment = request.POST['comment']
        location = request.POST['location']
        memory = Memory(memory_name=memory_name, comment=comment, location=location, owner=request.user)
        memory.save()
        return redirect('place-list')
    return render(request, 'place/add.html', context)
