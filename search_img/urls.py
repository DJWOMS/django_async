from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ListImageView.as_view(), name='list'),
    path('download/', views.search_save, name='download'),
    path('', views.SearchImageView.as_view())
]
