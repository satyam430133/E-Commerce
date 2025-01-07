from django.shortcuts import render,redirect
from django.views import View

class Cards(View):
    def get(self,request):
        return render(request,'cards.html')
    
    def post(self,request):
        return redirect('cards')