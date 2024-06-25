from django.forms import BaseModelForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView , DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
import uuid

class BlogList(ListView):
    model = Blog
    context_object_name = 'bloglist'
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

class CreatePost(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'ab/create.html'
    fields = ('title','content','image',)
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.title
        blog_obj.slug = title.replace(' ','-') + '-' + str(uuid.uuid4())
        blog_obj.save()
        return redirect('index')
   
def Read(request, slug):
    blog = Blog.objects.get(slug=slug)
    user = request.user
    already_liked = Like.objects.filter(blog=blog,user=user)
    if not already_liked:
        liked = True
    else:
        liked = False
    form = CommentForm()
    cmt_list = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.blog = blog
            cmt.user = user
            cmt.save()
            return HttpResponseRedirect(reverse('r',args={slug}))

    data = {'blog':blog, 'form':form,'comment_all':cmt_list,'liked':liked}
    return render(request,'ab/read.html',data)

def liked_post(request,pk):
    user = request.user
    blog = Blog.objects.get(pk=pk)
    already_liked = Like.objects.filter(blog=blog,user=user)
    if not already_liked:
        like_post = Like(blog=blog,user=user)
        like_post.save()
        return HttpResponseRedirect(reverse('r',args={blog.slug}))

def unliked_post(request,pk):
    user = request.user
    blog = Blog.objects.get(pk=pk)
    already_liked = Like.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('r',args={blog.slug}))

class UserBlogs(LoginRequiredMixin,TemplateView):
    template_name = 'ab/myBlogs.html'

class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ('title','content','image')
    template_name = 'ab/editBlog.html'
    def get_success_url(self,**kwargs):
        return reverse_lazy('r',kwargs={'slug':self.object.slug})
    

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'ab/del.html'
    success_url = reverse_lazy("user_blogs")