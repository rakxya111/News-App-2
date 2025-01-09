from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from newsroom.forms import CommentForm, ContactForm,NewsletterForm
from newsroom.models import Contact, Post,Category, Tag
from django.views.generic import ListView,DetailView,View,TemplateView
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q

class HomeView(ListView):
    model = Post
    template_name = "newsroom/home.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-published_at") [:5]


    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
       
        context["featured_posts"] = Post.objects.filter(
        published_at__isnull=False, status="active"
        ).order_by("-published_at")


        context["photography"] = Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-views_count")[:6]



        return context
    

class PostByCategoryView(ListView):
    model = Post
    template_name = "newsroom/list/list.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status="active",
            category__id=self.kwargs["category_id"],
        ).order_by("-published_at")
        return query
    
class PostByTagView(ListView):
    model = Post
    template_name = "newsroom/list/list.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status="active",
            tag__id=self.kwargs["tag_id"],
        ).order_by("-published_at")
        return query

class PostDetailView(DetailView):
    model = Post
    template_name = "newsroom/detail/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False, status="active"
        )
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        obj.views_count += 1
        obj.save()

        context["related_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active", category=obj.category
        ).exclude(id=obj.id).order_by("-published_at")[:3]

        context["previous_post"] = (
            Post.objects.filter(
            published_at__isnull=False, status="active",id__lt=obj.id
            ).order_by("-id")
            .first() )
        
        context["next_post"] = (
            Post.objects.filter(
            published_at__isnull=False, status="active",id__gt=obj.id
            ).order_by("id")
            .first() )
        
        
        return context
    
class ContactView(View):
    template_name = "newsroom/contact/contact.html"
    
    def get(self,request):
            return render(request,self.template_name)
   
    def post(self,request):
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request,"Sucessfully Submitted your query . We will contact you soon."
                )
                return redirect("contact")
            else:
                messages.error(
                    request,
                    "Cannot submit your query. Please make sure all fields are valid. ",
                )

                return render(
                    request,
                    self.template_name,
                    {"form":form}
                )

        
class CommentView(View):
     def post(self,request,*args,**kwargs):
          form = CommentForm(request.POST)
          post_id = request.POST["post"]
          if form.is_valid():
               form.save()
               return redirect("post-detail",post_id)
          
          post = Post.objects.get(pk=post_id)
          return render(
               request,
               "newsroom/detail/detail.html",
                {"post":post,"form":form},
          )

class NewsletterView(View):
     def post(self,request):
          is_ajax = request.headers.get("X-Requested-With")
          if  is_ajax == "XMLHttpRequest":
               form = NewsletterForm(request.POST)
               if form.is_valid():
                    form.save()
                    return JsonResponse(
                         {
                              "success" : True,
                              "message" : "Successfully Subscribed to the NewsLetter",

                         },
                         status=201,
                    )
               else:
                    return JsonResponse(
                         {
                              "success" : False,
                              "message" : "Cannot Subscribe to the NewsLetter"
                         },
                         status=400,
                    )
          else:
            return JsonResponse(
                 {
                      "success":False,
                      "message":"Cannot process, Must be an AJAX XMLHttpRequest",
                 },
                 status=400,
            )

               
class PostSearchView(View):
     template_name = "newsroom/list/list.html"

     def get(self,request,*args,**kwargs):
          query = request.GET["query"]
          post_list = Post.objects.filter(
               (Q(title__icontains=query) | Q(content__icontains=query))
               & Q(status="active")
               & Q(published_at__isnull=False)
            ).order_by("-published_at")
          
          page = request.GET.get("page",1)
          paginate_by = 3
          paginator = Paginator(post_list,paginate_by)
          try:
               posts = paginator.page(page)
          except:
               posts = paginator.page(1)
          
          return render(
               request,
               self.template_name,
               {"page_obj":posts,"query":query},
          )

class AboutView(TemplateView):
    template_name = "newsroom/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
    
        return context