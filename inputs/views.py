from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from .models import Baser
from .forms import InputForm

def home(request):
    basers = Baser.objects.all()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/allbase/')
    else:
        form = InputForm()
    return render(request, 'home.html', {'form' : form})

def allbase(request):
    basers = Baser.objects.all()
    return render(request, 'allbase.html', {'basers': basers})

def info(request):
    return render(request, 'info.html')

class Counter:
    count = 0
    def increment(self):
        self.count += 1
        return ''
    def decrement(self):
        self.count -= 1
        return ''
    def double(self):
        self.count *= 2
        return ''
#def base_enter(request):
