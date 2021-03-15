from django.urls import path, include
from .views import homepage


app_name='home'
urlpatterns = [
    path('', homepage, name="homepage"),
]