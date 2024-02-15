from django.shortcuts import render, get_object_or_404

from main.models import Bible, Bible_jang
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import random

# Create your views here.

def index(request):
    rand = Bible.objects.order_by("?").first()
    context = {'rand':rand}
    return render(request, 'main/index.html',context)

def page(request):
    list = Bible_jang.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(list, 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    context = {'list':list, 'page_obj':page_obj}
    return render(request, 'main/page.html',context)

def nav(request):
    return render(request, 'main/nav.html')
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        bibles = Bible_jang.objects.filter(book__contains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'bibles': bibles})
    else:
        return render(request, 'main/search.html')

def detail(request, post_id):
    bible_detail = get_object_or_404(Bible_jang, pk=post_id)
    return render(request, 'main/detail.html', {'bible_detail': bible_detail})

def select(request, ):
    return render(request, 'main/select.html', )


def selected_page(request):
    if request.method == 'POST':
        submit = request.POST['submit']
        bible_select = Bible_jang.objects.filter(book__contains=submit)
        return render(request, 'main/selected_page.html',{'submit': submit, 'bible_select': bible_select} )
    else:
        return render(request, 'main/selected_page.html')