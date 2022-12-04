from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Members
from .models import Login

# Create your views here.
def myfirst(request):
    return render(request,'myfirst.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=Login.objects.get(username=username)
        if user.password==password:
            return HttpResponseRedirect(reverse('index'))
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=Login(username=username, password=password)
        user.save()
        return HttpResponseRedirect(reverse('login'))
    
    return render(request,'register.html')    

def index(request):
    mymembers=Members.objects.all().values()
    template = loader.get_template("index.html")
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    if request.method=='POST':
        first=request.POST['firstname']
        last=request.POST['lastname']
        member=Members(firstname=first, lastname=last)
        member.save()
        return HttpResponseRedirect(reverse('index'))
    template=loader.get_template("add.html")
    return HttpResponse(template.render({},request))

def delete(request,id):
    member=Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    member=Members.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'mymember': member,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))