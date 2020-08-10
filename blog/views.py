from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
'''
all_posts = [
    {
        'auther': 'James',
        'title':'How to learn Django quickly',
        'content':'In this post I will teach you how to learn Django quickly',
        'date_posted':'Dec 24,2019 10:00 AM'
    },
    {
        'auther': 'Tom',
        'title':'Python JSON',
        'content':'How to deal with Python JSON',
        'date_posted':'Dec 23,2019 1:00 PM'
    },
    {
        'auther': 'Pintu',
        'title':'How Django static folder works',
        'content':'In this post I will teach you how to learn Django static quickly',
        'date_posted':'Dec 23,2019 1:00 PM'
    },
    {
        'auther': 'Rinku',
        'title':'Python Bootstrap',
        'content':'How to deal with Bootstrap in Python',
        'date_posted':'Dec 26,2019 1:00 PM'
    }

]
'''


def index(request):
    data = {
        'posts':Post.objects.all()
    
    }
    return render(request,'home.html',data)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html' #<app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = '/login/'
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    