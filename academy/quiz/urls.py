try:
    from django.conf.urls import url,path
except ImportError:
    from django.urls import re_path as url, path

from .views import QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake,CategoryByQuizList,category_quiz_filter

urlpatterns = [
    url(r'^$',
        view=CategoryByQuizList.as_view(),
        name='quiz_index'),

    url('progress/',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url('marking/',
        view=QuizMarkingList.as_view(),
        name='quiz_marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=QuizDetailView.as_view(),
        name='quiz_start_page'),

    path('<int:pk>/take/',QuizTake.as_view(),name='quiz_question'),
    # url(r'^category/(?P<pk>[\d.]+)/$',view=category_quiz_filter,name='category_quiz_filter'),
    path('category/<str:slug>',category_quiz_filter,name='category_quiz_filter')
]
