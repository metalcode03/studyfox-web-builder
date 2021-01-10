from django.urls import path, include
from . import views as v

app_name='blog'

urlpatterns = [
    path('', v.IndexView.as_view(), name='home'),
    path('list/', v.PostListView.as_view(), name='post-list'),
    path('search/', v.SearchView.as_view(), name='search'),
    path('create/', v.PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/', v.PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', v.PostUpdateView.as_view(), name='post-udate'),
    path('post/<pk>/delete/', v.PostDeleteView.as_view(), name='post-delete'),
]
