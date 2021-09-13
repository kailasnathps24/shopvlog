from django.shortcuts import render, get_object_or_404
from shopapp. models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def home(request,c_slug=None):
    c_page=None
    prodt = None

    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=product.objects.filter(category=c_page,available=True)
    else:

        prodt = product.objects.all().filter(available=True)

    cat=categ.objects.all()

    paginator=Paginator(prodt,2)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        p=paginator.page(page)
    except(EmptyPage,InvalidPage):
        p=paginator.page(paginator.num_pages)


    return render(request,'index.html',{'pro':prodt,'ct':cat,'pg':p})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'item.html',{'pro':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'pro':prod,'qr':query})

# Create your views here.
