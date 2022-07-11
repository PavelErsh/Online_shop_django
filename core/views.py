from django.shortcuts import render
from core.models import Item

# Create your views here.
def main(request):
    items = Item.objects.all()
    return render(request, 'main.html', {'items':items})
