from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')


# about page
def about(req):
    return render(req, 'about.html')


# blog page
def blog(req):
    return render(req, 'blog.html')