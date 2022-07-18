from django.shortcuts import render
from urllib import request
from core.models import Item

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


         

