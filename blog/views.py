from django.shortcuts import render, redirect

from .models import EditBlog
from .forms import MDForm

# Create your views here.
def index(request):
    """主页"""
    blogs = EditBlog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blog/index.html', context)

def blogs(request, blog_id):
    """查看具体笔记内容"""
    blog = EditBlog.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/blog.html', context)

def new_blog(request):
    """新建笔记"""
    if request.method != 'POST':
        form = MDForm()
    else:
        form = MDForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

    context = {'form': form}
    return render(request, 'blog/new_blog.html', context)

def edit_blog(request, blog_id):
    """编辑已有笔记"""
    blog = EditBlog.objects.get(id=blog_id)
    if request.method != 'POST':
        form = MDForm(instance=blog)
    elif 'del' in request.POST:
        form = None
        blog.delete()
        return redirect('blog:index')
    else:
        form = MDForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

    context = {'blog': blog, 'form': form}
    return render(request, 'blog/edit_blog.html', context)
