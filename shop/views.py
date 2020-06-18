from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .bqcode import SaveBQCodetoFnm
import sys, os

def product_list(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(available=True)
  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
  return render(
    request,
    'shop/product/list.html',
    {'category': category,
    'categories': categories,
    'products': products}
  )

def product_detail(request, id, slug):
  product = get_object_or_404(
    Product,
    id=id, slug=slug,
    available=True
  ) 

  SaveBQCodetoFnm(
    'code39', 
    str(product.bqcode), 
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + \
    '/shop/static/img/bqcode/' + \
    str(product.bqcode) + '.png'
  )

  return render(
    request,
    'shop/product/detail.html',
    {'product': product}
  )