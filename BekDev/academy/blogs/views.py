from django.shortcuts import render
from .models import BlogModel, CommentBlogModel, ReplyCommentBlogModel

# Create your views here.
def blogs(request):
    blogs = BlogModel.objects.all()
    return render(request, 'blogs/blogs.html', {'blogs':blogs})

def blog_detail(request, pk):
    blog = BlogModel.objects.get(id=pk)
    return render(request, 'blogs/blog_detail.html', {'blog':blog})