from django.shortcuts import render
from urllib import request
from core.models import Item
from core.forms import ItemForm
from django.shortcuts import redirect

# Create your views here.
def main(request):

    if request.method == 'POST':
        first_num = request.POST.get('first')
        second_num = request.POST.get('second')
        items = Item.objects.filter(price__range=(first_num, second_num))
        return render(request, 'main.html', {'items':items})

    else:
        items=Item.objects.all()
        return render(request, 'main.html', {'items':items})

def form(request):
    forma = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            print("test")
            form.save()
            return redirect('main')
    return render(request, 'add.html', {'forma':forma})
         

