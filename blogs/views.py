from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import PostForm

def index(request):
    """ This view will show posts in data base """

    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts':posts}
    return render(request, 'blogs/index.html', context)

def add_post(request):
    """ This view will display form for new post """

    if request.method != 'POST':
        # No data submitted; create blank form
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form':form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """ This view edits an existing post """

    post = get_object_or_404(BlogPost, pk=post_id)

    if request.method != 'POST':
        # Initial request; populate fields
        form = PostForm(instance=post)
    else:
        # POST request; updating data with data in fields
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index', args=[post_id]))
    
    context = {'post':post, 'form':form}
    return render(request, 'blogs/edit_post.html', context)
