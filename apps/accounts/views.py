from django.shortcuts import render


def index(request):
    print('index', request)
    context = {}
    return render(request, 'index.html', context)
