from django.shortcuts import render, get_object_or_404 ,redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Reviewpost, Reviewcomment
from .forms import BannerUpdateForm, CommentForm, ReviewUpdateForm, CommentreviewForm
from taggit.models import Tag



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def reviewcomment_approve(request, pk):
    comment = get_object_or_404(Reviewcomment, pk=pk)
    comment.approve()
    return redirect('review-detail', pk=comment.post.pk)


def reviewcomment_remove(request, pk):
    comment = get_object_or_404(Reviewcomment, pk=pk)
    comment.delete()
    return redirect('review-detail', pk=comment.post.pk)

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


def add_comment_to_reviewpost(request, pk):
    post = get_object_or_404(Reviewpost, pk=pk)
    if request.method == "POST":
        form = CommentreviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('review-detail', pk=post.pk)
    else:
        form = CommentreviewForm()
    return render(request, 'add_comment_to_reviewpost.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class ReviewpostListView(ListView):
    model = Reviewpost
    template_name = 'blog/review.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class ReviewDetailView(DetailView):
    model = Reviewpost

class PostDetailView(DetailView):
    model = Post


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Reviewpost
    form_class = ReviewUpdateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = BannerUpdateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = BannerUpdateForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ReviewpostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reviewpost
    form_class = ReviewUpdateForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ReviewpostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reviewpost
    success_url = '/review/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

    
def review(request):
    paginate_by = 5
    context = {
        'reviews': Reviewpost.objects.all()
    }
    return render(request, 'blog/review.html', context)

def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(RestuarantName__icontains=query)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchsouthfood(request):
    allPosts = Post.objects.filter(is_southfood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchnorthfood(request):
    allPosts = Post.objects.filter(is_northfood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchnoodlefood(request):
    allPosts = Post.objects.filter(is_noodlefood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchjapanfood(request):
    allPosts = Post.objects.filter(is_japanfood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchchinesefood(request):
    allPosts = Post.objects.filter(is_chinesefood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchbuffetfood(request):
    allPosts = Post.objects.filter(is_buffetfood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchfastfood(request):
    allPosts = Post.objects.filter(is_fastfood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchthaifood(request):
    allPosts = Post.objects.filter(is_thaifood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchsomtumfood(request):
    allPosts = Post.objects.filter(is_somtumfood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)

def searchcafefood(request):
    allPosts = Post.objects.filter(is_cafefood=True)
    params = {'allPosts': allPosts}
    return render(request,'blog/search.html', params)




