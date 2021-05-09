from django.contrib import admin
from .models import ProblemModel,ProblemAnswerModelUser,UserRatingSystem

admin.site.register(ProblemModel)
admin.site.register(ProblemAnswerModelUser)

admin.site.register(UserRatingSystem)