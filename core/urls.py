from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='registration'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('post/', views.PostView.as_view(), name='post'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/?id=<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name = 'core/logout.html'), name='logout'),
    # path('change-password/', auth_views.PasswordChangeView.as_view(
    #     template_name='user/change_password.html'), name='change_password'),
    # path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='password_change_done.html'), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='core/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='core/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='core/password_reset_complete.html'), name='password_reset_complete'),
]