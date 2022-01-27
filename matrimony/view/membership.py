from django.shortcuts import render

def membership(request):
    return render(request, 'matrimony/membershipplans.html')
    