from .models import Post, Comment
from .forms import NewPostForm, CommentForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404



class PostsListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status= 'pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.filter(active=True)
        return context


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list') 



class CommentCrateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        post_id = int(self.kwargs['post_id'])
        post = get_object_or_404(Post, id=post_id)

        obj.post = post

        return super().form_valid(form)






