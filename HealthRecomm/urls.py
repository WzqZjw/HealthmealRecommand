from django.contrib import admin
from django.urls import path, include
from accounts.views import login  # 导入登录视图

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='root'),  # 将根路径指向登录页面
    path('accounts/', include('accounts.urls')),  # 用户管理路由
    path('recipes/', include('recipes.urls')),  # 食谱推荐路由
]
