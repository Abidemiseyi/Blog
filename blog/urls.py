from asyncio import tasks
from tkinter import N
from unicodedata import name
from django.urls import path
from . import views
from .views import BlogList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete, Login, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', BlogList.as_view(), name='blogs'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('create/', BlogCreate.as_view(), name='blog-create'),
    path('update/<int:pk>/', BlogUpdate.as_view(), name='blog-update'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='blog-delete')
]
