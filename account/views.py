from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth import get_user_model
# user = get_user_model()
from account.models import Profile


# from account.models import Profile
# from django.conf import settings
# User = settings.AUTH_USER_MODEL

def login_request(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            nextUrl = request.GET.get('next', None)
            if nextUrl is None:
                messages.success(request, "Login Succesful!")
                return redirect("index")
            else:
                return redirect(nextUrl)
        else:
            messages.error(request, "Username or Password is not valid.")
            return render(request, "account/login.html")

    else:
        return render(request, "account/login.html")


def register_request(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        birthdate = request.POST.get("birthdate", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("repassword", None)
        gender = request.POST.get("gender", None)

        # if username and email and first_name and last_name is not None:
        # pass
        # else:
        # return render(request, "account/register.html", {"error": "Please annın nikahı"})

        if password == re_password:
            if Profile.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error": "Username has already exists."})
            else:
                if Profile.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {"error": "Email has already exists."})
                else:
                    user = Profile(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name, birthdate=birthdate,
                        gender=gender
                    )
                    try:
                        user.full_clean()
                    except Exception as e:
                        return render(request, "account/register.html", {"error": e.messages})#"there cannot be" koyulabılır 2z yerıne
                    user = Profile.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name, birthdate=birthdate,
                        gender=gender
                    )
                    user.is_active = True
                    user.save()
                    return redirect("login_request")
        else:
            return render(request, "account/register.html", {"error": "Passwords are not the same."})
    else:
        return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    messages.success(request, "You have been logging out.")
    return redirect("index")


def profile(request):
    return render(request, "account/profile.html")


def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Parola değiştirildi.")
            return redirect("changepassword")
        else:
            return render(request, 'account/changepassword.html', {"form": form})

    form = PasswordChangeForm(request.user)
    return render(request, 'account/changepassword.html', {"form": form})
