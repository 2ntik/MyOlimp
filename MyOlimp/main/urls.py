from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage, name='home'),
    path('suggestion_form', suggestion_view, name='suggestion'),
    path('success', success_view, name='success')
]
