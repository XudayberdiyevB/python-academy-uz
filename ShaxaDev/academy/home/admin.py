from django.contrib import admin
from .models import CardModel,HomeMaqolaModel,TagModel

# Register your models here.
admin.site.register(CardModel)
admin.site.register(HomeMaqolaModel)
admin.site.register(TagModel)