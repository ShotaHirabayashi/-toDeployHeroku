from django.shortcuts import render,redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages

# Create your views here.
def index(request):
    all_address = Address.objects.all
    return render(request,'index.html',{"all_address":all_address})

def home(request):
    return render(request,'home.html',{})


def add(request):
    if request.method == 'POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Address has been added'))
            return redirect('home')
        else:
            messages.success(request,('something wrong'))
            return render(request,'add_address.html',{})
    else:
        return render(request,'add_address.html',{})


def edit(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        form = AddressForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request,('Address has been added'))
            return redirect('index')
        else:
            messages.success(request,('something wrong'))
            return render(request,'edit.html',{})
    else:
        get_address = Address.objects.get(pk=list_id)
        return render(request,'edit.html',{"get_address":get_address})


def delete(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(pk=list_id)
        current_address.delete()
        messages.success(request,('Address has been added'))
        return redirect('index')
    else:
        messages.success(request,('something wrong'))
        return redirect('index')
