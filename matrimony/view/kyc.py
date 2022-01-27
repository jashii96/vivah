from django.shortcuts import render

def kyc(request):
    return render(request, 'matrimony/kyc.html')