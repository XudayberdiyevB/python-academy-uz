from django.urls import path
from .views import register,login_view,logout_view,profile
from django.contrib.auth import views as auth_views
app_name='account'

urlpatterns=[
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="account/password_reset.html",), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view( template_name="account/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view( template_name="account/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view( template_name="account/password_reset_complete.html"), name="password_reset_complete"),

    path('profile/', profile, name='profile'),
]