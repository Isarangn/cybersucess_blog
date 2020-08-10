from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
       form = UserRegistrationForm(request.POST)
       profile_form = UserProfileForm(request.POST)
       if form.is_valid() and profile_form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            user.profile.phone = profile_form.cleaned_data.get('phone')
            user.profile.save() 
            #form.save() 
            #profile_form.save()
            messages.success(request,f'Account Created Successfully \
                 for user {username} !!!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        profile_form = UserProfileForm() #request.POST

    return render(request,'register.html',{'form':form,'profile_form':profile_form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile details has been updated successifully.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'profile.html', context)