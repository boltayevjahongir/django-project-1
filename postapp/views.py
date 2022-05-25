from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Categorya
# Create your views here.

def home(req):
    return render(req, 'home.html')


# about page
def about(req):
    return render(req, 'about.html')


# blog page
def blog(req):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)  # Show 25 contacts per page.

    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(req, 'blog.html',
                  context={
                      'posts':page_obj
                  }
                  )

def blog_detail(req, id):

    # filter by id
    posts = Post.objects.get(id=id)

    # order by
    post_2 = Post.objects.all().order_by('-date')

    # view count
    posts.view_count+=1
    posts.save()

    cat = Categorya.objects.all()

    return render(req, 'blog_detail.html',
                  context={
                      'posts':posts,
                      'post_2':post_2,
                      'cat':cat
                  })