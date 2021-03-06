from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404, render

from .models import Category, Works

# Create your views here.

def index(request):

    category = Category.objects.filter(is_active =True)
    work = Works.objects.all()
    context={

        "category" : category,
        "work" : work,
    }
    return render(request,'index.html', context)





def details(request, id):

    works = Works.objects.get(id=id)
    similar  = Works.objects.filter(category=works.category)
    

    context={
        "similar" : similar,
        "works" : works,
       
    }
    return render(request,'details.html', context)

