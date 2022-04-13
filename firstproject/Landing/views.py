from django.shortcuts import render

# Create your views here.
# 2022.04.13 html + css 

def index(request):
    return render(request,'Landing/index.html')