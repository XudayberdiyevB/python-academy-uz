from django.urls import path
from .views import problems, problem_detail,my_result_problem,detail_answer_user

app_name='problems'
urlpatterns = [
    path('', problems, name='all'),
    path('<int:pk>/', problem_detail, name='detail'),
    path('problem-all-result/',my_result_problem,name='my_result'),
    path('answer-problem-detail/<int:pk>',detail_answer_user,name='answer_detail'),
]