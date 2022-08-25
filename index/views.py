from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


def login1(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('homepage')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={'form': form}
    )


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

        return redirect("register_done")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})


def register_done(request):
    return render(request, 'register_done.html')


def userspage(request):
    return render(request, 'userspage.html')


def logout(request):
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")


def save(self, *args, **kwargs):
    if not User.objects.filter(name=self.name).first():
        super(User, self).__init__(*args, **kwargs)