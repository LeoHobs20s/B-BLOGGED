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

def new_post(request):
    """ This view will display form for new post """

    if request.method != 'POST':
        # No data submitted; create blank form
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('index'))
    
    context = {'form':form}
    return render(request, 'blogs/new_post.html', context)