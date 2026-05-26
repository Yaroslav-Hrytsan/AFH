from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return HttpResponse("welcome to my blog")

def page(request, page_name):
    return HttpResponse(f"this is page {page_name}")

def go_home(request):
    # редірект на головну через reverse
    return HttpResponseRedirect(reverse('blog:home'))

def about(request):
    return HttpResponse(
        "it is about page. If you want to go to home page click <a href='/'>here</a>"
    )