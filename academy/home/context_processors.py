from .models import AdmingaXabar, UsergaJavob

def chatsupport(request):
    usermsg=None
    adminmsg=None
    if request.user.is_authenticated:
        usermsg = AdmingaXabar.objects.filter(user=request.user).first()
        adminmsg = UsergaJavob.objects.filter(send_to=request.user, savol=usermsg, is_answer=True).first()
    context = {
        'usermsg':usermsg,
        'adminmsg':adminmsg
    }    
    return context