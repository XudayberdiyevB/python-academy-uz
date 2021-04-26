from django.urls import path
from .views import homepage, team, tag_filter, card_detail

app_name='home'
urlpatterns = [
    path('', homepage, name="homepage"),
    path('message/<int:pk>/', card_detail, name="card_detail"),
    path('team/', team, name="team"),
    path('filter/<str:name>/',tag_filter,name='filter')
]