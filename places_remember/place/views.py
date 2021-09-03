from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def place_home(request):
    return render(request, 'place/home.html')


@login_required
def place_list(request):
    context = {
        'avatar_url' : request.user.social_auth.get().extra_data['avatar_url']
    }
    return render(request, 'place/list.html', context)
