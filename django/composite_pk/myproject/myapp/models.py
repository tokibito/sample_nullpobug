from django.db import models

class Product(models.Model):
    """製品"""
    name = models.CharField("名称", max_length=100)


class Order(models.Model):
    """注文"""
    reference = models.CharField("注文番号", max_length=20, primary_key=True)


class OrderLineItem(models.Model):
    """注文明細"""
    pk = models.CompositePrimaryKey("product_id", "order_id")
    product = models.ForeignKey(Product, verbose_name="製品", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name="注文", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="数量")
