from contextlib import redirect_stdout
# from inspect import _Object
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponse
from home.models import Form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          # Redirect to a success page.
          return redirect('/sign_in')
      else:
          # Return an 'invalid login' error message.
          return redirect('/')

    return render(request,'index.html')

def form(request):
    if request.method=='POST': 
        ename=request.POST.get('ename')
        email=request.POST.get('email')
        num=request.POST.get('num')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        comment=request.POST.get('comment')
        plans=request.POST.get('plans')
        form=Form(ename=ename,email=email,num=num,gender=gender,address=address,comment=comment,plans=plans)
        form.save()
        messages.success(request, 'Form has been submitted successfully.') 
    return render(request,'form.html')

def sign_in(request):
    if request.user.is_anonymous:
    #   user = request.id  
      return redirect('/')
    data=Form.objects.all()
    return render(request,'sign_in.html',{'data': data})

def logoutuser(request):
    logout(request)
    return redirect('/')

def delete(request,id):
    if request.method=='POST': 
     data=Form.objects.get(id=id).delete()
     messages.warning(request, 'Form has been deleted successfully.') 
     print(data)
     return HttpResponseRedirect('/sign_in')
     
def edit(request):
    data=Form.objects.all()
    return render(request,'/sign_in',{'data': data},{{'id':id}})

def update(request,id):
    if request.method=='POST': 
        ename=request.POST.get('ename')
        email=request.POST.get('email')
        num=request.POST.get('num')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        comment=request.POST.get('comment')
        plans=request.POST.get('plans')
        form=Form(id=id,ename=ename,email=email,num=num,gender=gender,address=address,comment=comment,plans=plans)
        form.save()
        messages.success(request, 'Form has been updated successfully.') 
        return HttpResponseRedirect('/sign_in')
    