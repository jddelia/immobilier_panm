from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator

class PostView(ListView):
    model = Post
    template_name = 'mainsite/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

def post(request, post_id):
    post_obj = get_object_or_404(Post, pk=post_id)
    more_imgs = post_obj.more_photos.split(',')
    context = {
        'post': post_obj,
        'more_imgs': more_imgs
    }
    return render(request, 'mainsite/location.html', context)
