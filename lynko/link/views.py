from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, LinkForm
from .models import Category, Link

@login_required
def links(request):
    category = request.GET.get('category', '')
    links = Link.objects.filter(created_by=request.user)

    if category:
        link = links.filter(category_id=category)

    return render(request, 'link/links.html', {
        'links': links,
        'category': category,
    })



@login_required
def categories(request):
    categories = Category.objects.filter(created_by=request.user)

    return render(request, 'link/categories.html', {
        'categories': categories
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
        'form': form,
        'title':'Create Link',
    })


@login_required
def edit_link(request, pk):
    link = get_object_or_404(Link, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)

        if form.is_valid():
            form.save()

            return redirect('/links/')
    else:
        form = LinkForm(instance=link)

        # Show only specific login user's categories in dropdown
        form.fields['category'].queryset = Category.objects.filter(created_by=request.user)

    return render(request, 'link/create_link.html', {
        'form': form,
        'title':'Edit Link',
    })


@login_required
def delete_link(request, pk):
    link = get_object_or_404(Link, created_by=request.user, pk=pk)
    link.delete()

    return redirect('/links/')


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
        'form': form,
        'title': 'Create Category',
    })


def edit_category(request, pk):
    # get_object_494() package is a shortcut to get things into the database.
    category = get_object_or_404(Category, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()

            return redirect('/links/categories/')
    else:
        # instance is use so that all the fields are automatically fill out in form.
        form = CategoryForm(instance=category)

    return render(request, 'link/create_category.html', {
        'form': form,
        'title': 'Edit Category',
    })


@login_required
def delete_category(request, pk):
    # get_object_494() package is a shortcut to get things into the database.
    category = get_object_or_404(Category, created_by=request.user, pk=pk)
    category.delete()

    return redirect('/links/categories/')