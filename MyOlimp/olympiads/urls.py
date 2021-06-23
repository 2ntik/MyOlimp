from django.urls import path
from . import views

urlpatterns = [
    path('', views.OlympiadListView.as_view(), name='olympiads'),
    path('<int:pk>', views.OlympiadDetailView.as_view(), name='olympiad_detail'),
    path('<int:pk>/edit', views.OlympiadEditView.as_view(), name='olympiad_edit'),
    path('create', views.OlympiadCreateView.as_view(), name='olympiad_create'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]