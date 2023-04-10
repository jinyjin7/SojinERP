from django.shortcuts import render, redirect
from .models import ProductModel,Stock
from .models import Outbound
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'erp/index.html')
    else:
        return redirect('/sign-in')
@login_required
def inbound(request):
    if request.method == 'GET':
        return render(request, 'erp/inbound_create.html')
    elif request.method == 'POST':
        product_code = request.POST.get('product_code', '')
        product_name = request.POST.get('product_name', '')
        product_descr = request.POST.get('product_descr', '')
        product_price = request.POST.get('product_price', '')
        product_size = request.POST.get('product_sizes', '')
        product_quantity = request.POST.get('product_quantity', '')
        if product_code=='' or product_name=='' or product_price=='' or product_quantity=='':
            return render('erp/inbound_create.html',{'error': '제품코드, 이름, 가격, 수량은 필수칸입니다.'})
        else:
            ProductModel.objects.create(product_code=product_code, product_name=product_name, product_descr=product_descr,
                                            product_price=product_price,product_size=product_size,product_quantity=product_quantity)
            product_list = ProductModel.objects.all()
            return redirect('/')
    else:
        return render('erp/inbound_create.html')


#출고
@login_required
def product_adding(request):
    if request.method == 'GET':
        produt_list = ProductModel.objects.all()
        return render(request, 'erp/product_adding.html',{'product_list':produt_list})
    elif request.method == 'POST':
        product_code = request.POST.get('product_code', '')
        product_size = request.POST.get('product_sizes', '')
        product_adding_quantity = request.POST.get('product_adding_quantity', '')

        if product_code == '' or product_adding_quantity == '' or product_size == '':
            return render(request, 'erp/product_adding.html', {'error': '제품코드, 수량, 사이즈는 필수칸입니다.'})

        else:
            product = ProductModel.objects.get(product_code=product_code,product_size=product_size)
            product.product_quantity += int(product_adding_quantity)
            product.save()
            product_list = ProductModel.objects.all()
            return redirect('/')
        # else:
        #     return render(request, 'erp/product_adding.html', {'error': '입고 수량이 유효하지 않습니다.'})
    else:
        return render(request, 'erp/product_adding.html')

@login_required
def outbound(request):
    if request.method == 'GET':
        produt_list = ProductModel.objects.all()
        return render(request, 'erp/outbound_create.html', {'product_list': produt_list})
    elif request.method == 'POST':
        product_code = request.POST.get('product_code', '')
        product_size = request.POST.get('product_sizes', '')
        outbound_quantity = request.POST.get('outbound_quantity', '')

        if product_code == '' or outbound_quantity == '' or product_size == '':
            return render(request, 'erp/outbound_create.html', {'error': '제품코드, 이름, 수량은 필수칸입니다.'})

        if not outbound_quantity.isdigit():
            return render(request, 'erp/outbound_create.html', {'error': '출고 수량을 숫자로 입력해주세요.'})
        else:
            product = ProductModel.objects.get(product_code=product_code, product_size=product_size)
            product.product_quantity -= int(outbound_quantity)
            product.save()
            product_list = ProductModel.objects.all()
            return redirect('/')
    else:
        print(0)
        return render(request, 'erp/outbound_create.html')



@login_required
def inventory(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            product_list = ProductModel.objects.all()
            return render(request, 'erp/inventory.html',{'product_list': product_list})
