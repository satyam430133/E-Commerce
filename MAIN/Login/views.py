from django.shortcuts import render,redirect
from django.db.models import Q
from django.views import View
from .models import *


class Login(View):
    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username and password:
            print('welcome')
            check = UserModel.objects.filter(username=username,password=password)
            if check:
                print('done')
                return redirect('index')
        return render(request,'login.html')
    
class Register(View):
    def get(self, request):
        return render(request,'register.html')
    
    def post(self,request):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserModel(email=email,username=username,password=password)

        return redirect('login')