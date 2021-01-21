from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import HttpResponseForbidden
import re
from _ast import Or
from django.contrib.auth.models import User
from software.models import Release
from tools.models import Tool
from products.models import Product
def va(request):
    
    branches = ["master", "develop"]

    for release in Release.objects.filter(title = "t9107_doc10_sw_va"):
        parser = re.compile(r".*/(feature/[^/]*)/.*")
        if parser.search(release.doc_path_html):
            branch = parser.match(release.doc_path_html)[1]
            if branch not in branches:
                branches.append(branch)
                
        parser = re.compile(r".*/(bugfix/[^/]*)/.*")
        if parser.search(release.doc_path_html):
            branch = parser.match(release.doc_path_html)[1]
            if branch not in branches:
                branches.append(branch)
        
        parser = re.compile(r".*/(pull_request/[^/]*)/.*")
        if parser.search(release.doc_path_html):
            branch = parser.match(release.doc_path_html)[1]
            if branch not in branches:
                branches.append(branch)

    context = {
        'branches' : branches
    }
    return render(request, 'va/list_branches.html', context)

def va_branch(request, branch_type):
    context = {
        'releases' : Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = branch_type)
    }
    return render(request, 'lsd/home.html', context)

def va_branch_name(request, branch_type, branch_name):
    context = {
        'releases' : Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = branch_type + "/" + branch_name)
    }
    return render(request, 'lsd/home.html', context)

def va_details_latest(request):
    context = {
        'release' : Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = "master")[0]
    }
    return render(request, 'software/software_release_details.html', context)

def va_details_latest_doc(request):
    release = Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = "master")[0]
    return redirect(reverse("lsd-home") + release.doc_path_html)

def va_details_latest_sw(request):
    release = Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = "master")[0]
    return redirect(reverse("lsd-home") + release.bin_path)

def va_details_nightly(request):
    context = {
        'release' : Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = "develop")[0]
    }
    return render(request, 'software/software_release_details.html', context)

def va_details_nightly_doc(request):
    release = Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = "develop")[0]
    return redirect(reverse("lsd-home") + release.doc_path_html)

def va_details_nightly_sw(request):
    release = Release.objects.order_by('-date').filter(title = "t9107_doc10_sw_va", doc_path_html__contains = "develop")[0]
    return redirect(reverse("lsd-home") + release.bin_path)
