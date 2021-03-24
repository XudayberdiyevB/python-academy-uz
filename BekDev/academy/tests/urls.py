from django.urls import path
from .views import exam

app_name = "tests"
urlpatterns = [
    path('', exam, name="tests")
]