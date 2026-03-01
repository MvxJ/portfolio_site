from django.urls import path
from blog import views

urlpatterns = [
    path(
        route='/',
        name='index',
        view=views.index,
     ),
    path(
        route="/posts",
        name='posts',
        view=views.posts,
    ),
    path(
        route="/posts/<slug:slug>",
        name='post',
        view=views.single_post,
    )
]