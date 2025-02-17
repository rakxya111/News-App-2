from django.urls import path
from newsroom import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("post-by-category/<int:category_id>/",views.PostByCategoryView.as_view(),name="post-by-category"),
    path("post-by-tag/<int:tag_id>/",views.PostByTagView.as_view(),name="post-by-tag"),
    path("post-detail/<int:pk>/",views.PostDetailView.as_view(),name="post-detail"),
    path("contact/",views.ContactView.as_view(),name="contact"),
    path("post-comment/",views.CommentView.as_view(),name="post-comment"),
    path("newsletter/",views.NewsletterView.as_view(),name="newsletter"),
    path("post-search/",views.PostSearchView.as_view(),name="post-search"),
    path("about/",views.AboutView.as_view(),name="about"),
]