from django.urls import path
from .views import blogs, blog_detail

app_name = "blogs"
urlpatterns = [
    path('', blogs, name="blogs"),
    path('<int:pk>/', blog_detail, name="blog_detail"),
]