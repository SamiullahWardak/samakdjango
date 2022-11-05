from multiprocessing import context
from turtle import title
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

from .forms import ProductForm, RawProductForm, product
from .models import product

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    myForm = RawProductForm(request.POST)
    if myForm.is_valid():
        print(myForm.cleaned_data)
    else:
        print(myForm.errors)
    
    context = {
        'form': form,
        'myForm': myForm
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, my_id):
    # obj = product.objects.get(id=my_id)
    try:
        obj = product.objects.get(id=my_id)
    except product.DoesNotExist:
        raise Http404
    context = {
        "obj" : obj
    }
    return render(request, "products/dynamic_product.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'obj' : obj
    }
    return render(request, 'products/product_delete.html', context)
    
# def product_create_view(request):
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_details_view(request):
    obj = [product.objects.get(id=1),
           product.objects.get(id=2),
        #    product.objects.get(id=3),
           ]
    context = {
        'object': obj
    }
    return render(request, "products/product_details.html", context)

def product_list_view(request):
    queryList = product.objects.all()
    context = {
        'querySet':queryList
    }
    return render(request, "products/product_list.html", context)