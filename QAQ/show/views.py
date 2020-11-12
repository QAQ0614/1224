from django.shortcuts import render

def homepage(request):
  foods = ['三明治套餐', '鬆餅套餐', '漢堡套餐']
  return render(request, 'index.html', {'foods':foods})

def food(request, kind):
  return render(request, 'food.html', {'kind':kind})