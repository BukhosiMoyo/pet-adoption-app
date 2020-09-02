from django.shortcuts import render
from django.http import Http404
from .models import Pet

def home(request):
    pets = Pet.objects.all()


    context ={'pets':pets}
    return render(request, 'adoptions/home.html', context)


def pet_details(request, pet_id):

    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not found')
    context={'pet':pet}
    return render(request, 'adoptions/pet_details.html', context)

def aboutAuthor(request):
    context={}
    return render(request, 'adoptions/about.html', context)
