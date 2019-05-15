from django.shortcuts import render
from .forms import ClientForm


def registration(request):
    form = ClientForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    return render(request, 'registration/registration.html', locals())


def home(request):
    return render(request, 'registration/home.html', locals())


def about(request):
    return render(request, 'registration/about.html', locals())


def contact(request):
    return render(request, 'registration/contact.html', locals())
