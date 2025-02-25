from .models import Post
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy



class PostsListView(generic.ListView):
    # with below command database give you all objects, but we dont want this.
    # model = Post --> if this model dont define then go to get_queryset function.
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status= 'pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


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












# def posts_list_view(requset):
#     # post_list = Post.objects.all() --> show all Posts(Published / Draft / etc)

#     # filter function say that what type of post show in Blog Page.
#     post_list = Post.objects.filter(status= 'pub').order_by('-datetime_modified')
#     # Post.objects.filter(title= 'BF8') --> then show me Posts with this title in Page.

    
#     return render(requset, 'blog/posts_list.html', {'posts': post_list})



# def post_detail_view(request, pk):
#     # post_detail = Post.objects.get(pk=pk)
#     post = get_object_or_404(Post, pk=pk) # get better result from error with this code.     
    
#     return render(request, 'blog/post_detail.html', {'post': post})



# def post_create_view(request):

#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid(): # if was True
#             form.save()
#             return redirect('posts_list')    # url address.
#     else: # if request method was
#         form = NewPostForm()
            
#     return render(request, 'blog/post_create.html', {'form': form})




# def post_update_view(request, pk):  # edit_view

#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post) # if user input was GET then return None that is 
#                                                         # invalid, and if user fill it then return Edited Post.
#                                                 # form = NewPostForm(requset.POST, instance=post)
     
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')


#     return render(request, 'blog/post_create.html', {'form': form})
    


    # def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
    
#     return render(request, 'blog/post_delete.html', {'post': post})


