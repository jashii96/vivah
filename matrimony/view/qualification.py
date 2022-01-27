from django.shortcuts import render

def qualification(request):
    return render(request, 'matrimony/qualification.html')

def physical_attribute(request):
    return render(request, 'matrimony/physical_attribute.html')

def personal_info(request):
    return render(request, 'matrimony/personal_info.html')

def photo_album(request):
    return render(request, 'matrimony/photo_album.html')

def horoscope(request):
    return render(request, 'matrimony/horoscope.html')

def family_details(request):
    return render(request, 'matrimony/family_details.html')


def habits(request):
    return render(request, 'matrimony/habit.html')