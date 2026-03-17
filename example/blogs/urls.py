from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, SignUpView

urlpatterns = [
    path('', PostListView.as_view(), name='blogs_home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]