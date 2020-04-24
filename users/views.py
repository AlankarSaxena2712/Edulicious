from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import mail_admins, send_mail
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from .models import PhoneSave

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            number = form.cleaned_data.get('phone_number')
            stud_class = form.cleaned_data.get('student_class')
            phnsave = PhoneSave(name=username, phone_number=number, stud_class=stud_class)
            
            send_mail(
                f"New User {username} registered",
                f'Please go to the admin site and verify that {username} is authentic or not.',
                'edulicious2020@gmail.com',
                ['edulicious2020@gmail.com', 'saxenaalankar42@gmail.com'],
                fail_silently=False,
            )
            # mail_admins(subject=f"New User {username} registered", message=f"Please go to the admin site and verify that {username} is authentic or not ", fail_silently=False)
            phnsave.save()
            form.save()
            messages.info(request, f'{username} registerd on EDULICIOUS. You will be notified about your verification!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})