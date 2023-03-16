from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CategoryForm, LinkForm
from .models import Category, Link

@login_required
def links(request):
    links = Link.objects.filter(created_by=request.user)

    return render(request, 'link/links.html', {
        'links': links,
    })

@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()

            return redirect('/dashboard/')
    else:
        form = LinkForm()

        # Show only specific login user's categories in dropdown
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)

    return render(request, 'link/create_link.html', {
        'form': form
    })



# Create category will only be available if the user is login.
@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()

            return redirect('/dashboard/')
    else:
        form = CategoryForm()

    return render(request, 'link/create_category.html', {
        'form': form
    })