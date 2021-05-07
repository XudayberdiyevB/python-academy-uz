from django import template
from ..models import ProblemModel,ProblemAnswerModelUser
from django.contrib.auth.models import User
register = template.Library()


@register.filter
def problem_check_filter(pk,u):
	prob=ProblemModel.objects.get(id=pk)
	res=ProblemAnswerModelUser.objects.filter(problem=prob)
	if res.exists():
		res1=res.filter(is_correct=True,user=u)
		if len(list(res1))!=0:
			return 3
		else:
			return 2
	else:
		return 1

   
