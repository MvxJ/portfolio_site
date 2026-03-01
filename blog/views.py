from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request=request,
        template_name="blog/index.html",
        context={}
    )


def posts(request):
    pass


def single_post(request, slug):
    pass