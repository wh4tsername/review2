from django.shortcuts import render
from .forms import ClientForm


def registration(request):
    form = ClientForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    return render(request, 'registration/registration.html', locals())
