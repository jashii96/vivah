from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from matrimony.forms import Loginform,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages


@login_required(login_url='login')
def myprofile(request):
    form = Loginform()
    context = {
        'form':form
    }
    return render(request,'matrimony/my_profile.html', context = context)



# Update it here
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm() 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated Successfully')
            return redirect('myprofile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, template_name='matrimony/profile.html', context = context)