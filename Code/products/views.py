#SPDX-License-Identifier: BSD-3-Clause

'''
views.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Hentges <lsd@luetze.de>
'''
from django.shortcuts import render
from products.models import Product

def product_list(request):
    """
    This function renders a list of products.
    """
    article_no_list = []
    product_temp_list = []
    for product in Product.objects.all():
        if product.article_number not in article_no_list:
            article_no_list.append(product.article_number)
            product_temp_list.append(product)

    context = {"products": product_temp_list}
    return render(request, "products/product_list.html", context)


def product_details(request, article_number):
    """
    This function renders products with different versions, filtered through its
    article number and sorted through the revision of an article.
    """
    specific_products = Product.objects.order_by("-article_revision").filter(
        article_number=article_number
    )
    context = {"products": specific_products}
    return render(request, "products/product_details.html", context)


def product_details_latest(request, article_number):
    """
    This function renders the newest revision of a single product.
    """
    product_temp_list = []
    product_temp_list.append(
        Product.objects.order_by("-article_revision").filter(
            article_number=article_number
        )[0]
    )
    context = {"products": product_temp_list}
    return render(request, "products/product_details.html", context)


def product_details_revision(request, article_revision):
    """
    This function renders the revision of a product.
    """
    product_temp_list = []
    product_temp_list.append(Product.objects.filter(article_revision=article_revision)[0])
    context = {"products": product_temp_list}
    return render(request, "products/product_details.html", context)
