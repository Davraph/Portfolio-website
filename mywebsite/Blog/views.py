from urllib import request
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from .models import STATUS, Post, Comment
from django.views.generic import ListView
from django.views import View
from django.db.models import Q
from django.urls import reverse
from .forms import CommentForm
from django.http import HttpResponseRedirect


# Class based view




class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-created_on"]
    context_object_name = "all_posts"
    paginate_by = 2



  

    
    #query the recent posts
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    

    # def index(request):
    #     if 'q' in request.get:
    #         q = request.get['q']
    #         # posts = Post.objects.filter(title__icontains=q)
    #         multiple_q = Q(Q(title__iexact=q))
    #         posts = Post.Data.objects.filter(multiple_q)
        
    #     else:   
    #         posts = Post.objects.all()
            
    #     context = {
    #         'posts' : posts
    #     }
    #     return render(request, 'blog/index.html', context)

    
class SinglePostView(View):
 
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
       
        
        

     # Update the view count on each visit to this post.
        if post:
           post.views = post.views + 1
           post.save()


        context = {
            'post': post,
             "comment_form": CommentForm(),
             "comments": post.comments.all().order_by("-id"),
             "comments_count": Comment.objects.filter(post=post).count()
             
            
        }
        
        

        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
       



        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail", args=[slug]))


        context = {
                "post": post,
                "comment_form": comment_form,
                "comments": post.comments.all().order_by("-id"),
               
                

        }
        return render(request, "blog/post-detail.html", context)
        
