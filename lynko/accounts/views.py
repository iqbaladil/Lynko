from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Login user
            authenticate(username=user.username, password=user.password)

            if user is not None:
                login(request, user)

                # Redirect to home page after successfully login
                return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {
        'form': form
    })