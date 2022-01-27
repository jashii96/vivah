from django.shortcuts import render,redirect
from matrimony.forms import Dataform
from django.views import View


class dataview(View):
    def get(self,request):
        form = Dataform()
        return render(request, template_name= "matrimony/data.html", context={'form' : form })

    def post(self, request):
        form = Dataform(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')

        return render(request, template_name= "matrimony/data.html", context={'form' : form })
