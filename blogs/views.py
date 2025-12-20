from django.shortcuts import render, get_object_or_404

from .models import BlogPost

def index(request):
    """ This view will show posts in data base """

    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts':posts}
    return render(request, 'blogs/index.html', context)
