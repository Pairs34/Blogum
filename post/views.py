from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,get_object_or_404

# Create your views here.
from post.models import Post


def home_view(request):
    if request.user.is_authenticated:
       context = {"isim":"Ali"}
    else:
       context ={"isim":"Misafir"}
    return render(request,"home.html",context)

def post_index(request):
    posts = Post.objects.all()
    return render(request,"post/index.html",{"posts":posts})

def post_detail(request,post_id):
    secilen_post = get_object_or_404(Post,id=post_id)
    context = {
        "post" : secilen_post
    }
    return render(request,"post/detail.html",context)

def post_create(request):
    return HttpResponse('Post Index')
def post_delete(request):
    return HttpResponse('Post Index')
def post_update(request):
    return HttpResponse('Post Index')