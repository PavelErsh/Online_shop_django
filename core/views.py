from django.shortcuts import render

# Create your views here.
def main(request):
    var = "hello"
    return render(request, 'main.html', {'var':var})
