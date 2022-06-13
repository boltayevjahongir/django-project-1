from django.urls import path
from .views import home, about, blog, blog_detail, contact, category

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('blog_detail/<int:id>', blog_detail, name='blog_detail'),
    path('category/<int:id>', category, name='category'),
]