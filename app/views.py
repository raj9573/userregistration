from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login,logout


from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # Set the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # Link the profile to the user
            profile.save()

            # Redirect to a success page or login page
            return redirect('userlogin')
             # Replace 'login' with the URL name of the login view
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def userlogin(request):

    if request.method  =='POST':

        un = request.POST['username']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('home')




    return render(request,'user_login.html')

# @login_required
def home(request):
    current_user = request.user     


    return render(request,'home.html',{'current_user':current_user})

@login_required
def user_logout(request):
    logout(request)

    return redirect('userlogin')