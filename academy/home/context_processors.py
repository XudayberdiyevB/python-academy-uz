from .models import AdmingaXabar, UsergaJavob

def chatsupport(request):
	usermsg=None
	adminmsg=None
	if request.user.is_authenticated:
		usermsg = AdmingaXabar.objects.filter(user=request.user).first()
		adminmsg = UsergaJavob.objects.filter(send_to=request.user, savol=usermsg, is_answer=True).first()

	key=request.POST.get('supportchat')
	context = {
		'usermsg':usermsg,
		'adminmsg':adminmsg
	}
	if key:
		AdmingaXabar.objects.create(text=key,user=request.user)
		context['msg']='Xabaringiz yuborildi!'

	return context
