from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm,ProfileForm,UserRegisterForm
from django.views import generic
from .models import *
from django.db.models import Avg


# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'projects/index.html'
