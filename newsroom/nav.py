from django.shortcuts import render
from newsroom.models import Category, Tag, Post

def navigation(request):
    tags = Tag.objects.all()
    catgories = Category.objects.all()
    catgories1 = Category.objects.all()[:5]
    catgories2 = Category.objects.all()[:3]
    
    business_category = Category.objects.get(id=5)
    featured_business_post = Post.objects.filter(
                published_at__isnull=False, status="active", category=business_category
            ).order_by("-published_at").first()
    featured_business_posts = Post.objects.filter(
                published_at__isnull=False, status="active", category=business_category
            ).order_by("-published_at")[:5]
    
    
    fashion_category = Category.objects.get(id=4)
    
    featured_fashion_post = Post.objects.filter(
                published_at__isnull=False, status="active", category=fashion_category
            ).order_by("-published_at").first()
    
    featured_fashion_posts = Post.objects.filter(
                published_at__isnull=False, status="active", category=fashion_category
            ).order_by("-published_at")[:5]
    
    
    technology_category = Category.objects.get(id=2)
    featured_technology_post = Post.objects.filter(
                published_at__isnull=False, status="active", category=technology_category
            ).order_by("-published_at").first()
    featured_technology_posts = Post.objects.filter(
                published_at__isnull=False, status="active", category=technology_category
            ).order_by("-published_at")[:5]
    
    
    sports_category = Category.objects.get(id=6)
    featured_sports_post = Post.objects.filter(
                published_at__isnull=False, status="active", category=sports_category
            ).order_by("-published_at").first()
    featured_sports_posts = Post.objects.filter(
                published_at__isnull=False, status="active", category=sports_category
            ).order_by("-published_at")[:5]
    
   
    popular_posts = Post.objects.filter(
                published_at__isnull=False, status="active"
            ).order_by("-published_at")[:4]
    
    latest_posts = Post.objects.filter(
                published_at__isnull=False, status="active"
            ).order_by("-published_at")[:5]
    
    sponser = Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-views_count").first()
    
    return {
        "tags": tags,
        "categories": catgories,
        "popular_posts": popular_posts,
        "latest_posts": latest_posts,
        "categories1": catgories1,
        "categories2": catgories2,
        "featured_business_post": featured_business_post,
        "featured_business_posts": featured_business_posts,
        "featured_fashion_post": featured_fashion_post,
        "featured_fashion_posts": featured_fashion_posts,
        "featured_technology_post": featured_technology_post,
        "featured_technology_posts": featured_technology_posts,
        "featured_sports_post": featured_sports_post,
        "featured_sports_posts": featured_sports_posts,
        "sponser": sponser,

    }


      