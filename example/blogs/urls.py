from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SignUpView,
    DocumentuploadView,
    PostDetailView,
    toggle_like,
    toggle_bookmark,
    ProfileView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blogs_home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/like/', toggle_like, name='post_like'),
    path('posts/<int:pk>/bookmark/', toggle_bookmark, name='post_bookmark'),
    path('documents/upload/', DocumentuploadView.as_view(), name='document_upload'),
    path('profile/', ProfileView.as_view(), name='profile'),
]