from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/comments/', views.PostCommentsDetailView.as_view(), name='post_comments_detail'),
    path('<int:pk>/body/', views.PostBodyDetailView.as_view(), name='post_body_detail')
]