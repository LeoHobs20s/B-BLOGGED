from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View

from .models import BlogPost
from .forms import PostForm

def index(request):
    """ This view will show posts in data base """

    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts':posts}
    return render(request, 'blogs/index.html', context)


class NewPostView(View):
    form_class = PostForm
    template_name = 'blogs/add_post.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('index'))


# @login_required
# def edit_post(request, post_id):
#     """ This view edits an existing post """

#     post = get_object_or_404(BlogPost, pk=post_id, owner=request.user)
    
#     if request.method != 'POST':
#         # Initial request; populate fields
#         form = PostForm(instance=post)
#     else:
#         # POST request; updating data with data in fields
#         form = PostForm(instance=post, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
    
#     context = {'post':post, 'form':form}
#     return render(request, 'blogs/edit_post.html', context)

class UpdatePostView(View):
    form_class = PostForm
    template_name = 'blogs/edit_post.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(BlogPost, pk=post_id)

        if post.owner != request.user:
            raise Http404
        
        form = self.form_class(instance=post)
        return render(request, 'blogs/edit_post.html', {'form':form, 'post':post})
    
    def post(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(BlogPost, pk=post_id)

        form = self.form_class(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'blogs/edit_post.html', {'form':form, 'post':post})