from django.shortcuts import render
from blog.models import Post,Category
# Create your views here.
def home(request):
    posts=Post.objects.all()[:11]
    cats=Category.objects.all()
    data={ 'posts':posts,'cats':cats
    }
    return render(request,'home.html',data)
def base(request):
    #load alll the post from databases
    return render(request,'base.html')

def post(request,url):
    posts=Post.objects.get(url=url)
    cats=Category.objects.all()
    return render(request,'post.html',{'posts':posts,"cats":cats})

def aboutview(request):
        return render(request,'about.html')

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html",{"cat":cat,"posts":posts})
