from django.urls import path
from .views import *

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('edit', update_profile, name='edit'),
    path('register', register, name='register'),
    path('change_password', password_change_view, name='change_password'),

]
