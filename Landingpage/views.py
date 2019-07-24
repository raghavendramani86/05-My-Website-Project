from django.shortcuts import render, redirect
from django.http import HttpResponse
from Landingpage import forms

# imports for login logic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    data = {
        'key': ''
    }
    return render(request,'Landingpage/index.html',data)

def register(request):
    user_form = forms.UserForm()
    profile_form = forms.ProfileForm()
    details_form = forms.DetailsForm()

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        profile_form = forms.ProfileForm(request.POST)
        details_form = forms.DetailsForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and details_form.is_valid():
            # handling user information
            user_form = user_form.save(commit=False)
            user_form.set_password(user_form.password)
            user_form.save()

            # handling profile information
            profile = profile_form.save(commit=False)
            profile.user = user_form
            profile = profile.save()

            # handling detail information
            details_form = details_form.save()
            return redirect('user_login')
        else:
            HttpResponse('information invalid!')

    data = {
        'user_form': user_form,
        'profile_form': profile_form,
        'details_form': details_form,
    }

    return render(request,'Landingpage/register.html',data)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # this will authenticate the above credentials
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                print('1')
                value = login(request,user)
                print('success',value)
                return redirect('landing')
            else:
                print('hi, now this is invalid data')
                return HttpResponse('Invalid')
        else:
            print('Invalid Credentials')
            return redirect('user_login')
    else:
        return render(request,'Landingpage/user_login.html')

@login_required
def user_logout(request):
    logout(request)
    print('you are now logged out. Thank you for visiting this page')
    return redirect('user_login')

def landing(request):
    data = {

    }
    return render(request,'Landingpage/landing.html',data)
