from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """注册界面"""
    if request.method != 'POST':
        # 显示空的新注册表单
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blog:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)