from django.urls import path
from .views import blogs, blog_detail,blog_write_user,blog_own_user,blog_own_user_detail

app_name = "blogs"
urlpatterns = [
    path('', blogs, name="blogs"),
    path('<int:pk>/', blog_detail, name="blog_detail"),
    path('write-blog/',blog_write_user,name='blog_write_user'),
    path('own_blogs/',blog_own_user,name='blog_own_user'),
    path('own_blogs/<int:pk>/',blog_own_user_detail,name='blog_own_user_detail')

]