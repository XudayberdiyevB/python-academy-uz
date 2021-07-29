from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import CategoryBlog, BlogModel, CommentBlogModel, ReplyCommentBlogModel

class CategoryBlogModelTest(TestCase):
    def setUp(self):
        blog_categ=CategoryBlog.objects.create(category_name="Djangodan maqolalar",
                                    category_info="django framework bo'yicha qiziqarli maqolalar")
        author=User(username="bekzod")
        author.save()
        blog=BlogModel.objects.create(category_blog_id=1,title="Pythondan maqola1",text="absdefghijkl", author=author)

    def test_category_blog(self):
        blog_categ=CategoryBlog.objects.get(id=1)
        expected_categ_name=blog_categ.category_name
        expected_categ_info=blog_categ.category_info
        self.assertEqual(expected_categ_name,'Djangodan maqolalar')
        self.assertEqual(expected_categ_info,"django framework bo'yicha qiziqarli maqolalar")

    def test_category_exists_url(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)

    def test_blog_content(self):
        blog_categ = CategoryBlog.objects.get(id=1)
        blog=BlogModel.objects.get(id=1,category_blog=blog_categ)
        expected_blog_title=blog.title
        expected_blog_text=blog.text
        self.assertEqual(expected_blog_title,'Pythondan maqola1')
        self.assertEqual(expected_blog_text,'absdefghijkl')