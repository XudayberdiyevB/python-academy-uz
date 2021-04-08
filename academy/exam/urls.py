from django.urls import path
from .views import exam, exam_detail, test_results

app_name = "exam"
urlpatterns = [
    path('', exam, name="exam"),
    path('exam/<int:pk>', exam_detail, name="detail"),
    path('exam/<int:pk>/test-results', test_results, name="result")
]