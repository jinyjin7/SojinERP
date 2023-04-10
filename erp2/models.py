from django.db import models
from django.contrib.auth.models import AbstractUser


# 상품(상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드)
class ProductModel(models.Model):
    class Meta:

        db_table = "my_product"

    product_code = models.CharField(max_length=256, default='')
    product_name = models.CharField(max_length=50, default='')
    product_descr = models.TextField(default='')
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    product_size = models.CharField(choices=product_sizes, max_length=1)
    product_quantity = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
    input_date = models.DateTimeField(auto_now=True)
    output_date = models.DateTimeField(auto_now=True)

#제품등록 및 입고
class Inbound(ProductModel):
    inbound_quantity = models.IntegerField()


class Product_adding(ProductModel):
    product_adding_quantity = models.IntegerField()
    adding_date = models.DateTimeField(auto_now_add=True)

# 제품출고
class Outbound(ProductModel):
    Outbound_quantity = models.IntegerField()
    Outbound_date = models.DateTimeField(auto_now_add=True)

# def __str__(self):
#     return self.code
#

#제품이 0개가 되었을때 제품없애기
class Stock(models.Model):
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
# 입고(상품, 수량, 입고 날짜, 금액 필드를 작성)

#인벤토리
class Inventory(ProductModel):
    inbound_quantity = models.IntegerField()


