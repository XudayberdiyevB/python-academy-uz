from django.urls import path
from .views import problems, problem_detail

app_name='problems'
urlpatterns = [
    path('', problems, name='all'),
    path('<slug:slug>', problem_detail, name='detail')
]