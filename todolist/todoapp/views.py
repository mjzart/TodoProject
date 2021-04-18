from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todoitem

# Create your views here.
def index(request):
    todo_item_list = Todoitem.objects.all()
    return render(request, 'index.html', {
        'todo_item_list': todo_item_list
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