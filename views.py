import datetime
import json
import os

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import \
    UserCreationForm  # استيراد نموذج انشاء مستخدم
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateUserForm, adminproduct, reviewss
from .models import *
from .utils import cartData, cookieCart, guestOrder

     # لاجبار المشاهد لتسجيل الدخول


def product(request, id):#لعرض تفاصيل المنتج
    product=Product.objects.get(id=id)
    customer = request.user.customer

    related_products=Product.objects.filter(ram=product.ram).exclude(id=id)[:3]   
    dataa = cartData(request)
    cartItems = dataa['cartItems'] 

    if request.method == 'POST':
         add_comment = reviewss(request.POST)
         reviews= add_comment.save(commit=False)
         reviews.product=product
         reviews.customer= customer
         reviews.save()
         messages.success(request,'your review was successfully submitted!')

    context={
        'product':product
        ,'related':related_products,
        'cartItems':cartItems
        ,'reviews':reviewss()
    }
    return render(request,'pages/product.html',context);
# Create your views here.
def pagelogin(request):
      if request.user.is_authenticated:
            return redirect('index')
      else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password= request.POST.get('password')
            user =authenticate(request, username= username, password= password)  
            if user is not None:
                login(request , user)
                return redirect('index')
            else:
                messages.info(request,'Username OR password is incorrect')
        return render(request,'pages/login.html',{})        
def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
                form=CreateUserForm()
                if request.method == "POST":
                 form=CreateUserForm(request.POST)
                if form.is_valid():
                    user= form.save()
                    Customer.objects.create(
                        user = user,
                        name = user.username,
                        email = user.email
                    )    
                    Order.objects.get_or_create(customer=user.customer,complete=False)

                    username =form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for '+ username)
                    return redirect('login')
                return render(request,'pages/register.html',{'form':form})        
def index(request):
 
    # return HttpResponse('hello ')
        data = cartData(request)
        cartItems = data['cartItems'] #ليظهر جانب السلة عدد العناصر الي فيها اذا كان المستخدم ضيف
        related_products=Product.objects.all()[:10]   
        accessory=Product.objects.filter(category='accessory')[:4]   
        if request.method == 'POST':
         add_product = adminproduct(request.POST, request.FILES)
         if add_product.is_valid():
            add_product.save();
        return render(request,'pages/index.html',{'prod':Product.objects.filter(index='i').filter(category='photo'),
            'laptops':Product.objects.filter(index='i').filter(category='computer'),'cartItems':cartItems,
            'forms':adminproduct(),'related':related_products,'accessory':accessory,'reviews':review.objects.all
            ,'customer':Order.objects.all,'shipping':ShippingAddress.objects.all,'customerr':Customer.objects.all().count(),
             'review':review.objects.all().count()});


def about(request):
    return render(request,'pages/about.html');
 
def cart(request):
        data = cartData(request)

        cartItems = data['cartItems']
        order = data['order']
        items = data['items']

        context = {'items':items, 'order':order, 'cartItems':cartItems}
        return render(request, 'pages/cart.html', context)

@login_required(login_url='login')
def checkout(request):
        data = cartData(request)
        
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']

        context = {'items':items, 'order':order, 'cartItems':cartItems}
        return render(request,'pages/checkout.html',context);


def products(request):
   data = cartData(request)
   cartItems = data['cartItems']
   return render(request,'pages/products.html',{'pro':Product.objects.all(),'laptops':Product.objects.filter(index='p').filter(category='computer'),'cartItems':cartItems});
def laptops(request):
   data = cartData(request)
   cartItems = data['cartItems']
   return render(request,'pages/laptops.html',{'laptops':Product.objects.all().filter(category='computer'),'cartItems':cartItems});

def updateItem(request):#لاضافة المنتج الى الكارت باستخدام json
  try:
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order = Order.objects.filter(customer=customer, complete=False).first()

    orderItem ,created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
      orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
      orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
      orderItem.delete()

    return JsonResponse('Item was added', safe=False)
  except json.decoder.JSONDecodeError:
      # 👇️ this runs
      print('The string does NOT contain valid JSON')
      
def processOrder(request):#checkout
        transaction_id = datetime.datetime.now().timestamp()
        try: 
            data = json.loads(request.body)

            if request.user.is_authenticated:
                customer = request.user.customer
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
            else:
                customer, order = guestOrder(request, data)

            total = float(data['form']['total'])
            order.transaction_id = transaction_id

            if total == order.get_cart_total:
                order.complete = True
            order.save()

            if order.shipping == True:
                ShippingAddress.objects.create(
                    customer=customer,
                    order=order,
                    address=data['shipping']['address'],
                    city=data['shipping']['city'],
                    state=data['shipping']['state'],
                    zipcode=data['shipping']['zipcode'],
                )
            return JsonResponse('Payment submitted..', safe=False)
        except json.decoder.JSONDecodeError:
            print('The string does NOT contain valid JSON')





def chatbot(request):
    
    #  datas=json.loads(request.body)
    #  options=datas["options"]
    #  options2=enumerate(options,start=1)

        ram=Product.objects.all()
        data1 = serialize("json",ram)
        datas=json.dumps(data1)
        datas2=json.loads(data1)
        # my_dict ={i: datas2[i] for i in range(len(datas2))}
        # for i  in range(len(my_dict)):
       

        return JsonResponse(data1,safe=False)
def search(request):
    dataa = cartData(request)
    cartItems = dataa['cartItems']
	
    q=request.GET['q']
    data=Product.objects.filter(name__icontains=q)
    return render(request,'pages/search.html',{'data':data, 'cartItems':cartItems})  
def error(request): 
    return render(request,'parts/error.html')       
def update(request,id):#لتعديل الادمن
 product_id=Product.objects.get(id=id)
 if request.method == 'POST':
    product_save=adminproduct(request.POST,request.FILES,instance=product_id)#ال اي دي مشان تجبلي بيانات المنتج الي ضغطت عليه
    if product_save.is_valid():
            product_save.save()
            return redirect('/')
 else:     #هي الي لتتحقق بالبداية لاني ال post لما بضغط عالاضافة    
    product_save = adminproduct(instance=product_id)
    
 return render(request,'pages/update.html',{'form':product_save})
def delete(request,id):
    product_delete=get_object_or_404(Product , id=id)
    if request.method == 'POST':
        product_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')



