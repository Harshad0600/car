from django.shortcuts import render, redirect
# from .models import cservice
# from .models import LoginInfo
from .models import *   
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'index.html')

def service(request):
    return render(request,'services.html')

def project(request):
    return render(request,'project.html')

# def Nopage(request):
#     return render(request,'404.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# def login_page(request):
#     return render(request, 'login.html')

# def signup(request):
#     return render(request, 'signup.html')



def booking(request):

    if request.method=="POST":
        username=request.POST.get("uname")
        usermail=request.POST.get("mail")
        usercontact=request.POST.get('mobile')
        userservice=request.POST.get('option')
        usernote=request.POST.get('note')

        print(username,usermail,usercontact,userservice,usernote)

    # try:
    #     usercontact = int(usercontact)
    # except ValueError:
    #     messages.error(request, 'Please enter a valid phone number.')
    #     return render(request, 'contact.html')
    # try:
    #     record = cservice.objects.create(
    #         name=username,
    #         mail=usermail,
    #         number=usercontact,
    #         service=userservice,
    #         message=usernote
    #     )
    #     record.full_clean()  # This will run model validation
    #     record.save()
    #     messages.success(request, 'Your booking has been submitted successfully.')
    #     return redirect('contact')
    # except ValidationError as e:
    #     messages.error(request, f'An error occurred: {e}')
    #     return render(request, 'contact.html')

        record=cservice.objects.create(name=username,mail=usermail,number=usercontact,service=userservice,message=usernote)
        record.save()
        # messages.success(request, 'Your booking has been submitted successfully.')
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')
    




def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('lname')
        password = request.POST.get('lpass')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Log the login data
            LoginInfo.objects.create(
                user=user,
                username=username,
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )

             # Add success message
            messages.success(request, 'Successfully logged in')
            return redirect('home') 
        else:
            messages.error(request, 'Username is not registered.<br> Please signup First.', extra_tags='red')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    

def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        terms_agreed = request.POST.get('terms_agreed') == 'on'

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'signup.html')
        
        if not request.POST.get('terms_agreed'):
            messages.error(request, 'You must agree to the terms and conditions.')
            return render(request, 'signup.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Create the SignupInfo instance
        SignupInfo.objects.create(user=user, username=username, email=email, terms_agreed=terms_agreed)
        
        # Log the user in
        user = authenticate(username=username, password=password1)
        if user is not None:
            auth_login(request, user)

        return redirect('login')

        # return redirect('home')
    else:
        return render(request, 'signup.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')

# @login_required
# def home_view(request):
#     username = request.user.username
#     return render(request, 'home.html', {'username': username})