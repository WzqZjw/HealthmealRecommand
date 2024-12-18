# 健康食谱推荐系统 🍽️  

**健康食谱推荐系统** 是一款基于用户个性化数据的智能食谱推荐平台。用户可通过输入身高、体重、性别、年龄、地区、是否可吃辣等信息，获取符合个人需求的健康食谱。系统采用 **Django** 和 **MySQL** 开发，提供简单易用、界面美观的用户体验。  

---

## 📋 功能介绍  

### 1. **用户管理**  
- **注册功能**：用户可以通过用户名、邮箱和密码进行注册。  
- **登录功能**：已注册用户可以通过用户名和密码登录系统。  
- **账户验证**：密码经过加密存储，确保数据安全。

### 2. **健康食谱推荐**  
- 根据用户输入的个性化信息推荐符合条件的健康食谱：  
   - **身高和体重**  
   - **性别** 和 **年龄**  
   - **地区** 和 **口味偏好（是否能吃辣）**  
- 提供食谱详细信息：  
   - 菜名、描述、热量等。  

### 3. **结果展示**  
- 推荐食谱以卡片式布局展示，包含动态效果与交互反馈。  
- 支持修改筛选条件，重新获取推荐结果。  
- 提供友好的错误提示（如无符合条件的食谱）。

---

## 🛠️ 技术栈  

- **后端**：Django（Python Web 框架）  
- **数据库**：MySQL  
- **前端**：HTML + CSS  
- **版本控制**：Git 和 GitHub  

---

## 🚀 安装与运行  

### **1. 克隆项目代码**  
使用 Git 将项目代码克隆到本地：  
```bash
git clone https://github.com/WzqZjw/HealthmealRecommand.git
cd HealthmealRecommand
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境（Windows）
venv\Scripts\activate

# 安装依赖包
pip install -r requirements.txt
3. 数据库配置
在 settings.py 中配置 MySQL 数据库连接：

python
复制代码
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'health_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}4. 数据迁移
bash
复制代码
python manage.py makemigrations
python manage.py migrate
5. 运行项目
启动开发服务器：

bash
复制代码
python manage.py runserver
访问项目：http://127.0.0.1:8000/📸 页面预览
登录页面
简洁美观的用户登录界面。
个人信息输入页面
用户可填写身高、体重、年龄、地区、口味偏好等信息。
推荐结果展示页面
以卡片形式展示推荐的健康食谱，包括菜名、描述和热量信息。
支持动态交互效果，增强用户体验。
🔍 项目结构
bash
复制代码
HealthRecomm/
│
├── accounts/                # 用户管理模块
│   ├── models.py            # 用户模型
│   ├── views.py             # 注册与登录视图
│   ├── urls.py              # 用户模块路由
│   └── templates/           # 用户模块模板
│
├── recipes/                 # 食谱推荐模块
│   ├── models.py            # 食谱数据模型
│   ├── views.py             # 推荐逻辑视图
│   ├── urls.py              # 食谱模块路由
│   └── templates/           # 食谱推荐模板
│
├── HealthRecomm/            # 项目配置
│   ├── settings.py          # 项目设置
│   ├── urls.py              # 根路由
│   └── wsgi.py              # WSGI 配置
│
├── db.sqlite3               # 数据库文件（开发环境）
├── manage.py                # Django 管理脚本
├── requirements.txt         # Python 依赖列表
└── README.md                # 项目说明文档
💡 作品亮点
个性化推荐：通过用户输入的多维度信息智能推荐健康食谱。
界面美观：现代化布局与动态交互效果，增强用户体验。
数据安全：用户密码经过加密存储，保障数据安全。
灵活扩展：数据库设计合理，便于添加新功能或扩展食谱数据。
