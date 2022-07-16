from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
import json
# Create your views here.
"""def index(request):
    objects = Product.objects.all()
    context = {'objects' : objects}
    return render(request,'product.html',context)"""
def index(request):
    products = Product.objects.all()
    print(products)
    #n=len(products)
    #NoSlides = ceil(n/4)
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        NoSlides = ceil(n / 4)
        allprods.append([prod ,range(1,NoSlides),NoSlides])
    #params = {'No. of Slides':NoSlides,'range':range(1,NoSlides),'product':products}
    #allprods=[[products , range(1,NoSlides) , NoSlides],
           #   [products , range(1,NoSlides) , NoSlides]]
    params = {'allprods':allprods}
    return render(request,'index.html',params)


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=='POST':
        print(request)
        name = request.POST.get('NAME','')
        email = request.POST.get('EMAIL','')
        phone = request.POST.get('PHONE','')
        desc = request.POST.get('DESC','')
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'contact.html')


def tracker(request):
    if request.method == 'POST':
        orderid = request.POST.get('orderid','')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderid,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp,'name':item.name})
                    response=json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'tracker.html')


def search(request):
    return render(request,'search.html')


def prodView(request,myid):
    #fetch product using id
    prod = Product.objects.filter(id=myid)
    print(prod)
    return render(request,'prodView.html',{'prod': prod[0]})


def checkout(request):
    global id, thank
    if request.method =='POST':
        print(request)
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone','')
        print(itemsJson,name,email,address,city,state,zip_code,phone)
        order=Order(items_json=itemsJson,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        update=OrderUpdate(order_id=order.order_id,name=order.name,update_desc="Your Order has been placed successfully")
        update.save()
        thank= True
        id=order.order_id
        return render(request,'checkout.html',{'thank': thank ,'id': id})
    return render(request,'checkout.html')

