from datetime import date
from typing import Dict

from django.shortcuts import render, get_object_or_404

from blog.models import Post


def extract_post_date(post: Dict):
    return post["date"]

def index(request):
    posts = Post.objects.all().order_by("-created_at")[:2]

    return render(
        request=request,
        template_name="blog/index.html",
        context={
            "recent_posts": posts
        }
    )


def posts(request):
    posts = Post.objects.all().order_by("-created_at")

    return render(
        request=request,
        template_name="blog/all-posts.html",
        context={
            "posts": posts
        }
    )


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(
        request=request,
        template_name="blog/post-detail.html",
        context={
            "post": post,
            'post_tags': post.tags.all(),
        }
    )