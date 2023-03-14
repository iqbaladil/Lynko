from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create category will only be available if the user is login.
@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            link = form.save(commit=False)
            link.create_by = request.user
            link.save()

            return redirect('/')
        else:
            form = CategoryForm()

    return render(request, 'link/create_category.html', {
        'form': form
    })