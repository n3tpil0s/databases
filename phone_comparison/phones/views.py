from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    phones = Phone.objects.all()
    return render(
        request,
        'catalog.html',
        context={'phones': phones}
    )
