from django.shortcuts import render
from home.models import CardModel,TagModel,HomeMaqolaModel

# Create your views here.

def homepage(request):
    card=CardModel.objects.all()[0]
    maqolalar=HomeMaqolaModel.objects.all()
    context={'card':card,'maqolalar':maqolalar}

    return render(request, 'home/index.html',context)