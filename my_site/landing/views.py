from django.shortcuts import render


def landing(request):
    name = "maggot"
    return render(request, 'landing/landing.html', locals())
