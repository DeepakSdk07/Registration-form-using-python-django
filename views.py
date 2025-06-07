from django.shortcuts import render, redirect
from .models import Datas

def home(request):
    mydata = Datas.objects.all()
    return render(request, 'home.html', {'datas': mydata})

def addData(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']

        obj = Datas(name=name, age=age, address=address, contact=contact, mail=mail)
        obj.save()
        return redirect('home')
    return redirect('home')

def updateData(request, id):
    mydata = Datas.objects.get(id=id)
    if request.method == "POST":
        mydata.name = request.POST['name']
        mydata.age = request.POST['age']
        mydata.address = request.POST['address']
        mydata.contact = request.POST['contact']
        mydata.mail = request.POST['mail']
        mydata.save()
        return redirect('home')
    return render(request, 'update.html', {'data': mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id) 
    mydata.delete()
    return redirect('home')