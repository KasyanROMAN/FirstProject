
from django.contrib import admin
from django.urls import path

from news import views

urlpatterns = [
    path('',views.news_home,name='news_home'),
    path('create/', views.create, name='create'),
    path('<int:pk>/',views.ArtilesDetailView.as_view(), name='news-details'),
    path('<int:pk>/update',views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete',views.NewsDeleteView.as_view(), name='news-delete'),
]
