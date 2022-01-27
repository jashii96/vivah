from django.shortcuts import render

def contact(request):
    return render(request, 'matrimony/contactus.html')