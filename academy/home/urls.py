from django.urls import path
from .views import homepage, team, tag_filter

app_name='home'
urlpatterns = [
    path('', homepage, name="homepage"),
    path('team/', team, name="team"),
    path('filter/<str:name>/',tag_filter,name='filter')
]