from django.shortcuts import render, redirect

from .models import EditBlog
from .forms import MDForm


# Create your views here.
def index(request):
    """主页"""
    blog = EditBlog.objects.last()
    context = {'last_blog': blog}
    return render(request, 'blog/index.html', context)


def blog(request, blog_id):
    """查看具体笔记内容"""
    blog = EditBlog.objects.get(id=blog_id)
    blog_next = blog.id + 1
    blog_last = blog.id - 1
    id_last = EditBlog.objects.last().id
    id_first = EditBlog.objects.first().id
    context = {'blog': blog, 'blog_next': blog_next, 'blog_last': blog_last, 'id_last': id_last, 'id_first': id_first}
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
        return redirect('blog:blogs')
    else:
        form = MDForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/{blog_id}')

    context = {'blog': blog, 'form': form}
    return render(request, 'blog/edit_blog.html', context)


def blogs(request):
    """博客总览"""
    blogs = EditBlog.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)


def about(request):
    """介绍页"""
    return render(request, 'blog/about.html')


def page_not_find(request, exception):
    """404"""
    return render(request, '404.html', status=404)


def error(request):
    """50x"""
    return render(request, '500.html', status=500)
