from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login
from django.contrib import messages
from .forms import UserRegisterFrom, UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.

@login_required
def show_user(request):
    user = User.objects.all()
    print(user)
    context = {
        'title': 'Sistema Getan dadus Bibleoteca',
        'sub_title': 'Dadus Utilizador',
        'user': user,

    }

    return render(request, 'user.html', context)

@login_required
def register(request):
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()  # Save the user data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utilizador "{username}" registadu ho sucessu...!')
            return redirect('user')  # Replace 'login' with the name of your login route
    else:
        form = UserRegisterFrom()
    
    context = {
        'title': 'Registu Utilizador',
        'sub_title': 'Registu Utilizador',
        'form': form
    }
    return render(request, 'register.html', context)


@login_required
def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hadia dadus Utilizador ho susesu!')
            return redirect('user')
    else:
        form = UpdateUserForm(instance=user)
    
    # Render context for both GET and invalid POST
    context = {
        'title': 'Sistema Getan dadus Bibleoteca',
        'sub_title': 'Update dadus Utilizador',
        'form': form
    }
    return render(request, 'update_user.html', context)


@login_required
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, 'Hamos dadus Utilizador ho susesu...!')
    return redirect('user')

@login_required
def Change_password(request):
    if request.method == "POST":
        current_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        password_confirm = request.POST["password_confirm"]

        user = request.user  # Get the currently logged-in user
        if user.check_password(current_password):
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                # Log the user back in after changing the password
                login(request, user)
                messages.success(request, "Your password has been successfully changed.")
                return redirect('change-password')
            else:
                messages.warning(request, "New password and confirmation password do not match.")
        else:
            messages.warning(request, "Your current password is incorrect.")

    context = {
        'title': 'Sistema Getan dadus Bibleoteca',
        'sub_title': 'Update Password'
    }
    return render(request, 'update_pass.html', context)


@login_required
def Reset_password(request,id):
        userData = get_object_or_404(User,id=id)
        password = make_password('password')
        userData.password=password
        userData.save()
        update_session_auth_hash(request, userData)
        messages.success(request, f'Password ba {userData.first_name} {userData.last_name} Reset ho Susesu!')
        return redirect('user')
    
