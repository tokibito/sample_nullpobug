# coding: utf-8
from django.shortcuts import render
from shop.models import Category, Item, Bundle


def no_prefetch_view(request):
    # prefetch_relatedを使わない場合
    bundles = Bundle.objects.all()
    return render(request, 'index.html', {'bundles': bundles})


def prefetch_view(request):
    # prefetch_relatedを使う場合
    bundles = Bundle.objects.prefetch_related('items__category')
    return render(request, 'index.html', {'bundles': bundles})
