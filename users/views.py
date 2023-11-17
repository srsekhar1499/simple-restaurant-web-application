from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    # form = UserCreationForm(request.POST or None)
    # if form.is_valid():
    #     username = form.cleaned_data.get('username')
    #     messages.success(request, f'Welcome {username}, your account is created.')
    #     return redirect('food:index')
    # return render(request, 'user/register.html', {'form':form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcomme {username}, your account is created successfully.')
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form' : form})



@login_required
def profilepage(request):
    return render(request, 'user/profile.html')