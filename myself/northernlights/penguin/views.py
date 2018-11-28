from django.shortcuts import render
from datetime import datetime
from .models import Goods

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def bstest(request):
    return render(request, 'bstest.html')

def exercise(request):
    text = 'this is test.'
    try:
        input_text = request.POST['input_text']
        print(input_text)
        text = input_text
    except:
        return render(request, 'exercise.html')
    now = datetime.now();
    context = {
        'text' : text,
        'time' : now,
    }
    return render(request, 'exercise.html', context)

def loop(request):
    e = {'a', 'b', 'c', 'd', 'E', 'f', 'g'}
    f = []
    f.append('orange')
    f.append('apple')
    f.append('banana')

    p = {2,3,5,4,7,9,1,13,15,17,18,21,24,25,31,37,45,47,56,58}

    return render(request, 'loop.html', { 'alp':e, 'fruits':f, 'natural': p } )

def query(request):
    queryset = Goods.objects.all()
    context = { "querysetsss":queryset }
    return render(request, 'query.html', context)