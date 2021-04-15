from django.shortcuts import render, redirect
from .models import BlogModel, CommentBlogModel, ReplyCommentBlogModel

# Create your views here.
def blogs(request):
    blogs = BlogModel.objects.all()
    return render(request, 'blogs/blogs.html', {'blogs':blogs})

def blog_detail(request, pk):
    blog = BlogModel.objects.get(id=pk)
    blog.count_of_view+=1
    blog.count_of_comment=blog.comment_blog.count()
    blog.save()
    if request.method == 'POST':
        if request.POST.get('comment')=='':
            redirect('blogs:blog_detail',pk=pk)
        else:
            if request.POST.get('comment_id') is not None:
                comment=CommentBlogModel.objects.get(id=request.POST.get('comment_id'))
                reply_com=ReplyCommentBlogModel(reply_comment=comment,author=request.user,text=request.POST.get('reply_comment'))
                reply_com.save()
            elif request.POST.get('comment') is not None:
                com=CommentBlogModel(blog=blog)
                com.author=request.user
                com.text=request.POST.get('comment')
                com.save()

        return redirect('blogs:blog_detail',pk=pk)

    return render(request, 'blogs/blog_detail.html', {'blog':blog})