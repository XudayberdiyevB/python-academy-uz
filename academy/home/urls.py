from django.urls import path
from .views import homepage, team

app_name='home'
urlpatterns = [
    path('', homepage, name="homepage"),
    path('team/', team, name="team"),
]