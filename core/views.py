from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from .models import Post
from django.contrib.auth.models import User

# dict = {
#     'posts': Post.objects.all()
# }

class PostView(LoginRequiredMixin ,ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'core/post.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'context', 'image']
    template_name = 'core/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin ,DetailView):
    model = Post
    template_name = 'core/post_detail.html'


class ProfileView(ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'core/profile.html'


def register(request):
    if request.method == ['POST']:
        form = UserRegistration(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = UserRegistration()
        context = {
            'form': form
        }
    return render(request, 'core/register.html', context)


def home(request):
    return render(request, 'core/home.html')