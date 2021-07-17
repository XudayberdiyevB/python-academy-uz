from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogModel, CommentBlogModel, ReplyCommentBlogModel,CategoryBlog
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from home.models import TagModel
from .forms import BlogUserModelForm

def blogs(request):
    # blogs = BlogModel.objects.filter(is_publish=True)
    blogs_by_category=CategoryBlog.objects.all()
    return render(request, 'blogs/blogs.html', {'blogs':blogs_by_category})

def blogs_category(request,pk):
    category=CategoryBlog.objects.get(id=pk)
    blogs=BlogModel.objects.filter(category_blog=category,is_publish=True)
    return render(request,'blogs/blog_list_category.html',{'blogs':blogs})

def blog_own_user_detail(request,pk):
    blog=BlogModel.objects.get(id=pk)
    if request.method=='POST' and 'saqlash' in request.POST:
        form=BlogUserModelForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_own_user')
    form=BlogUserModelForm(instance=blog)
    return render(request,'blogs/blog_own_detail.html',{'form':form,'blog':blog})


def blog_own_user(request):
    filter_user=BlogModel.objects.filter(author=request.user)
    paginator = Paginator(filter_user, 5)
    page = request.GET.get('page')
    try:
        filter_user = paginator.page(page)
    except PageNotAnInteger:
        filter_user = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        filter_user = paginator.page(paginator.num_pages)
    return render(request,'blogs/filter_own_blogs.html',{'filter_user':filter_user})

def blog_write_user(request): 
    form=BlogUserModelForm() 
    if request.method=='POST' 'blogwrite' in request.POST:
        form=BlogUserModelForm(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            if request.user.is_superuser:
                blog.is_publish=True
            blog.author=request.user
            blog.is_publish=False
            blog.create_date=datetime.now()
            if request.FILES['image']:
                blog.image=request.FILES['image']
            blog.save()
            print(blog)
            return redirect('blogs:blogs')
   
    return render(request,'blogs/blog_write_user.html',{'form':form})
from django.http import HttpResponse
def blog_detail(request, pk):
    most_blogs=BlogModel.objects.filter(is_publish=True).order_by('-count_of_view')
    blog = BlogModel.objects.get(id=pk)
    blog.count_of_view+=1
    blog.count_of_comment=blog.comment_blog.count()
    blog.save()
    if request.method == 'POST':
        if request.POST['comment']=='':
            redirect('blogs:blog_detail',pk=pk)
        else:
            if request.POST.get('comment_id') is not None:
                comment=CommentBlogModel.objects.get(id=request.POST.get('comment_id'))
                reply_com=ReplyCommentBlogModel(reply_comment=comment,author=request.user,text=request.POST.get('reply_comment'))
                reply_com.save()
            elif request.POST['comment'] is not None:
                CommentBlogModel.objects.create(blog=blog,author=request.user,text=request.POST['comment'])
                return HttpResponse('create')
        return redirect('blogs:blog_detail',pk=pk)

    return render(request, 'blogs/blog_detail.html', {'blog':blog,'most_blogs':most_blogs})
