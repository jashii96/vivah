import imp
from django.shortcuts import render,redirect
from matrimony.model.feedback import Feedback
from django.contrib import messages
def feedbacks(request):
    if request.method == 'GET':
        return render(request,'matrimony/feedback.html')
    else:
        postdata = request.POST

        name = postdata.get('name')
        email = postdata.get('email')
        phone = postdata.get('phone')
        subject = postdata.get('subject')
        description = postdata.get('description')

        feedback = Feedback(
            name =name,
            email = email,
            phone = phone,
            subject = subject,
            description = description
        )
        
        error_message = None

        if Feedback.is_exist(feedback):
            error_message = "Email Id Already Exists"
        else:
            feedback.save()
            messages.success(request, f"Your Feedback Saved Successfully")
            return redirect('feedback')

        data={
            'error':error_message
        }
        return render(request, 'matrimony/feedback.html',data)