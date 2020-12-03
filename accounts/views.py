from django.shortcuts import redirect, render
from .forms import UserRegForm, UserLoginForm, ProfileForm
from .models import User, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def user_reg_view(request, *args, **kwargs):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = UserRegForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            return redirect('main:preference')
    else:
        form = UserRegForm()
        context = {
            'forms': form,
        }
        return render(request, 'registrations/signup.html', context)


def user_login_view(request, *args, **kwargs):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        if next:
            return redirect(next)
        return redirect('main:preference')
    context = {
        'forms': form
    }
    return render(request, 'registrations/login.html', context)


def user_logout_view(request):
    logout(request)
    return redirect('/login')


@login_required
@transaction.atomic
def update_profile(request, username):
    user = User.objects.get(username=request.user)
    if request.user != user:
        return redirect('index')

    if request.method == 'POST':
        print(request.POST)
        form = ProfileForm(
            request.POST, instance=user.profile, files=request.FILES)
        if form.is_valid():
            form.save()
            # return redirect(reverse('accounts', kwargs={'username': user.username}))
            messages.success(
                request,
                'Your Profile was successfully updated!!'
            )
            return redirect('/profile/%s' % username)
        else:
            messages.error(request, 'please correct the error below.')
    else:
        form = ProfileForm(instance=user.profile)
        return render(request, 'profile/profile_edit.html', {'profile_form': form})
