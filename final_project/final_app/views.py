from django.shortcuts import render
from . models import store

# Create your views here.
def demo(request):
    obj=store.objects.all()
    return render(request,"index.html",{'result':obj})
