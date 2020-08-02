from django.shortcuts import render

# Create your views here.
def welcomeDashboard(request):
    return render(request, 'welcomeDashboard.html')

