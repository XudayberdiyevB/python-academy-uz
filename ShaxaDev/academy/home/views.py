from django.shortcuts import render
from .models import CardModel,TagModel,HomeMaqolaModel

# home page viewlari

def homepage(request):
    card=CardModel.objects.all()[0]
    maqolalar=HomeMaqolaModel.objects.all()
    context={'card':card,'maqolalar':maqolalar}
    return render(request, 'home/index.html',context)