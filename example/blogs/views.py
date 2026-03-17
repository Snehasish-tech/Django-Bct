from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import post, Document, Comment, Like, Bookmark, Profile, Category, Tag
from .forms import DocumentForm, PostForm, CommentForm, ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('post_list')
        return render(request, 'registration/signup.html', {'form': form})

class PostListView(LoginRequiredMixin, ListView):
    model = post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    login_url = 'login'

    def get_queryset(self):
        queryset = post.objects.order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.order_by('-uploaded_at')
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    template_name = 'post_form.html'
    form_class = PostForm
    success_url = reverse_lazy("post_list")
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = post
    template_name = 'post_form.html'
    form_class = PostForm
    success_url = reverse_lazy("post_list")
    login_url = 'login'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy("post_list")
    login_url = 'login'

class DocumentuploadView(LoginRequiredMixin, CreateView):
    model = Document
    template_name = 'document_form.html'
    form_class = DocumentForm
    success_url = reverse_lazy("document_upload")
    login_url = 'login'

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post_obj = get_object_or_404(post, pk=pk)
        comment_form = CommentForm()
        return render(
            request,
            'post_detail.html',
            {
                'post': post_obj,
                'comment_form': comment_form,
                'is_liked': Like.objects.filter(post=post_obj, user=request.user).exists(),
                'is_bookmarked': Bookmark.objects.filter(post=post_obj, user=request.user).exists(),
            },
        )

    def post(self, request, pk):
        post_obj = get_object_or_404(post, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post_obj
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
        return render(
            request,
            'post_detail.html',
            {
                'post': post_obj,
                'comment_form': comment_form,
                'is_liked': Like.objects.filter(post=post_obj, user=request.user).exists(),
                'is_bookmarked': Bookmark.objects.filter(post=post_obj, user=request.user).exists(),
            },
        )


@login_required
@require_POST
def toggle_like(request, pk):
    post_obj = get_object_or_404(post, pk=pk)
    like, created = Like.objects.get_or_create(post=post_obj, user=request.user)
    if not created:
        like.delete()
    return redirect('post_detail', pk=pk)


@login_required
@require_POST
def toggle_bookmark(request, pk):
    post_obj = get_object_or_404(post, pk=pk)
    bookmark, created = Bookmark.objects.get_or_create(post=post_obj, user=request.user)
    if not created:
        bookmark.delete()
    return redirect('post_detail', pk=pk)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(instance=profile)
        return render(
            request,
            'profile.html',
            {
                'form': form,
                'profile': profile,
                'user_posts': post.objects.filter(author=request.user).order_by('-created_at'),
                'user_documents': Document.objects.filter(uploaded_by=request.user).order_by('-uploaded_at'),
                'bookmarks': Bookmark.objects.filter(user=request.user).select_related('post'),
            },
        )

    def post(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(
            request,
            'profile.html',
            {
                'form': form,
                'profile': profile,
                'user_posts': post.objects.filter(author=request.user).order_by('-created_at'),
                'user_documents': Document.objects.filter(uploaded_by=request.user).order_by('-uploaded_at'),
                'bookmarks': Bookmark.objects.filter(user=request.user).select_related('post'),
            },
        )
