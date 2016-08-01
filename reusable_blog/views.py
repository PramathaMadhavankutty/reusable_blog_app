from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
# Create your views here.

def post_list(request):
    """
    Create a view that will return a
    list of post that were published prior to 'now'
    and render them to blog_posts.html template

    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "reusable_blog/blogposts.html",{'posts':posts})

def post_details(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "reusable_blog/postdetail.html", {'post': post})

def top_post(request):
    """
    Get a list of posts and order them
    by the number of views. Only return the top 5 posts.
    Render it to blogposts.html

    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:4]
    return render(request,"reusable_blog/blogposts.html",{'posts':posts})

def new_post(request):
	
    if request.method=="POST":
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details,post.pk)
    	else:

        	form= BlogPostForm()
    		return render(request,"reusable_blog/blogpostform.html",{'form':form})
	
    else:
	return render(request, 'reusable_blog/blogpostform.html',
                      {'form': form})


