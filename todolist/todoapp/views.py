from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todoitem
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def index(request):
    todo_item_list = Todoitem.objects.all()

    p =Paginator(todo_item_list, 4)



    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)


    return render(request, 'index.html', {
        'todo_item_list': page,
    })

def additem(request):
    item = Todoitem(item_title = request.POST['item_title'], item_data = request.POST['date'], item_done = ' ')
    print(request.POST['date'])
    item.save()
    return HttpResponseRedirect( reverse('todoapp:_index_'))

def delete_item(request, id):
    Todoitem.objects.filter(id = id).delete()
    return HttpResponseRedirect(reverse('todoapp:_index_'))

def complete_item(request, id):
    a = Todoitem.objects.get(id=id)
    print(a)
    a.item_done = 'done'
    a.save()
    return HttpResponseRedirect(reverse('todoapp:_index_'))

