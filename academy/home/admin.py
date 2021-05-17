from django.contrib import admin
from home.models import CardModel, TagModel, FAQModel

# Register your models here.
admin.site.register(CardModel)
admin.site.register(TagModel)
admin.site.register(FAQModel)