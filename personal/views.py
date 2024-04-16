from django.shortcuts import render

def index(request):

    context = {}

    context['title'] = 'Django tutorial'

    return render(request, 'personal/home.html', context)
