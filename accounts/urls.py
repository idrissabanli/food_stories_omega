from django.urls import path, re_path
from accounts.views import (
    RegisterView, StoriesLoginView, 
    ChangePasswordView, register, 
    login, user_profile, logout,
    Activate,
    ResetPasswordView,
    CustomPasswordResetConfirmView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', StoriesLoginView.as_view(), name='login'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
        Activate.as_view(), name='activate'),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
        CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
]