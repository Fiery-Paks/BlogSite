"""
URL configuration for blog project.
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.articles, name='articles'),
    path('article/<int:article_id>/', views.get_article, name='get_article')
]