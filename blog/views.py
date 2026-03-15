from datetime import date
from typing import Dict

from django.shortcuts import render

posts_data = [
    {
        "slug": "hike-in-mountains",
        "image": "mountains.jpeg",
        "author": "Post Author",
        "date": date(2026, 7, 25),
        "title": "Mountain hiking",
        "excerpt": "Very exciting hiking!",
        "content": """<p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>""",
    },
{
        "slug": "coding-exercise",
        "image": "coding.jpeg",
        "author": "Post Author",
        "date": date(2024, 3, 31),
        "title": "Coding challenge",
        "excerpt": "Very exciting coding challenge!",
        "content": """<p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>""",
    },
{
        "slug": "forest-run",
        "image": "woods.jpg",
        "author": "Post Author",
        "date": date(2018, 8, 12),
        "title": "Run in forest!",
        "excerpt": "Very exciting forest run!",
        "content": """<p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, ipsum vel fringilla maximus, velit ex eleifend leo, ac vestibulum velit dolor a tellus. Mauris sed iaculis risus. In laoreet pellentesque fermentum. Mauris quis nulla interdum, scelerisque magna in, tincidunt est. Maecenas tempor, lectus et malesuada sodales, tortor tortor tincidunt ipsum, vitae viverra turpis nibh facilisis elit. Nulla facilisi. Curabitur et consectetur sem, sollicitudin lacinia purus. Quisque erat ante, aliquet in dui at, pretium pharetra risus. Praesent ullamcorper metus ut lorem dignissim scelerisque.
        </p>""",
    }
]

def extract_post_date(post: Dict):
    return post["date"]

def index(request):
    sorted_posts = sorted(posts_data, key=extract_post_date)
    latest_posts = sorted_posts[-2:]

    return render(
        request=request,
        template_name="blog/index.html",
        context={
            "recent_posts": latest_posts
        }
    )


def posts(request):
    sorted_posts = sorted(posts_data, key=extract_post_date)

    return render(
        request=request,
        template_name="blog/all-posts.html",
        context={
            "posts": sorted_posts
        }
    )


def single_post(request, slug):
    post = next(post for post in posts_data if post["slug"] == slug)

    return render(
        request=request,
        template_name="blog/post-detail.html",
        context={
            "post": post
        }
    )