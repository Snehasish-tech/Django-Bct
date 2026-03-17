from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import login

# Create your views here.

class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
        return render(request, 'registration/signup.html', {'form': form})

class PostListView(LoginRequiredMixin, ListView):
    model = post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    login_url = 'login'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    template_name = 'post_form.html'
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")
    login_url = 'login'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = post
    template_name = 'post_form.html'
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")
    login_url = 'login'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy("post_list")
    login_url = 'login'