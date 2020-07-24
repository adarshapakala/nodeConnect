from django.shortcuts import render

def loginOrRegister(request):
    return render(request, 'loginOrRegister.html')