from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User

# 注册视图
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User

def register(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])

        # 检查用户名或邮箱是否已存在
        if User.objects.filter(username=username).exists():
            error = "用户名已存在！"
        elif User.objects.filter(email=email).exists():
            error = "邮箱已被注册！"
        else:
            User.objects.create(username=username, email=email, password=password)
            return redirect('login')  # 注册成功后跳转到登录页面

    return render(request, 'accounts/register.html', {'error': error})


# 登录视图
def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            return redirect('home')  # 登录成功跳转到首页
        else:
            error = "用户名或密码错误！"

    return render(request, 'accounts/login.html', {'error': error})