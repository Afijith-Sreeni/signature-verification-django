from django.shortcuts import render
from.models import signature_verification

# Create your views here.
def base(request):
    data=signature_verification.objects.all()
    return render(request, 'ram.html',{"data":data})
def abhi(request):
    return render(request, 'abhi.html')