from django.shortcuts import render
from .models import Recipe

def recommend(request):
    if request.method == 'POST':
        height = request.POST['height']
        weight = request.POST['weight']
        gender = request.POST['gender']
        age = request.POST['age']
        region = request.POST['region']
        spicy = request.POST['spicy']

        # 基于用户输入的条件查询推荐食谱
        recipes = Recipe.objects.filter(suitable_for=gender, region=region)

        # 如果用户不能吃辣，则进一步筛选（假设 description 包含 '辣' 关键词）
        if spicy == "否":
            recipes = recipes.exclude(description__icontains='辣')

        # 将结果返回前端
        return render(request, 'recipes/recommend.html', {'recipes': recipes})

    return render(request, 'recipes/input.html')
