from django.shortcuts import render, redirect
from User.forms import UserForm, UserProfileInfoForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required
def special(request):
    return HttpResponse("You are logged")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('okkkkkkkkkkkkk')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(('/home/'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
            print("fghjklfghjkl")
    else:
        return render(request, 'login.html', {})


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def ChangePasswordView(request):
    if request.method == 'POST':
        pform = ChangePasswordForm(request.POST, user=request.user)
        if pform.is_valid():
            user = pform.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/home/')
        else:
            messages.error(request, 'Correct the error below')
    else:
        pform = ChangePasswordForm(user=request.user)
        return render(request, 'change_password.html', {'pform': pform})


@login_required
def uprofile(request):
    if request.method == 'POST':
        uform = UserForm(data=request.POST, instance=request.user)
        if uform.is_valid():
            uform.save()
            return redirect('/home/')
    print(request.user)
    uform = UserForm(data=request.POST, instance=request.user)
    return render(request, 'profile.html', {"uform": uform})


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')