
from django.http import HttpResponse

def employee(request):
    return HttpResponse("Employe Page")

def profile(request):
    return HttpResponse('profile')