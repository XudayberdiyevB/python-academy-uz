from django import template
from ..models import BlogModel,CategoryBlog

from django.contrib.auth.models import User
register = template.Library()


@register.filter
def filter_count(pk):
	cat=CategoryBlog.objects.get(id=pk)
	blog_filter=BlogModel.objects.filter(is_publish=True,category_blog=cat).count()
	return blog_filter

   
