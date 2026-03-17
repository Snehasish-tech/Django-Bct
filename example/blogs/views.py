from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import post
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = post
    template_name = 'post_form.html'
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    model = post
    template_name = 'post_form.html'
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

class PostDeleteView(DeleteView):
    model = post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy("post_list")
