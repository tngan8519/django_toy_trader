from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Toy
from .forms import ToyCreateForm

# Create your views here.
def browse_view(request):
    toys = Toy.objects.all()
    context = {"toys":toys}
    return render(request,"toy/browse.html",context)

def create_toy_view(request):
    form = ToyCreateForm()
    if request.method == 'POST':
        form = ToyCreateForm(request.POST, request.FILES)
        form.name = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            # do other form related logic
            obj.user = request.user
            obj.save()
            return redirect('/toy')
    else:
        return render(request, 'toy/post.html', {"form": form})

def read_toy_view(request,toy_id):
    try:
        toy = Toy.objects.get(id = toy_id)
    except Toy.DoesNotExist:
        raise Http404
    context = {
        'toy': toy,
    }
    return render(request,"toy/detail.html",context)

def update_toy_view(request,toy_id):
    try:
        toy = Toy.objects.get(id = toy_id)
    except Toy.DoesNotExist:
        raise Http404
    form = ToyCreateForm(request.POST or None, instance = toy)
    if request.method == 'POST':
        form = ToyCreateForm(request.POST, request.FILES, instance = toy)
        if form.is_valid():
            form.save()
            return redirect(f"/toy/{toy_id}")
    context = {
        'toy': toy,
        'form':form
    }
    return render(request,"toy/edit.html",context)

def delete_toy_view(request, toy_id):
    try:
        toy = Toy.objects.get(id = toy_id)
    except toy.DoesNotExist:
        return redirect('/toy')
    toy.delete()
    return redirect('/toy')