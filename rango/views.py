from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm


def example_view(request):
    return HttpResponse('This is an example view.')


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    top_pages = Page.objects.order_by('-views')[:5]

    context_dict = {
        'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!",
        'categories': category_list,
        'top_pages': top_pages,
        'no_pages_message': "There are no pages present.",
        'pages': top_pages,
    }

    return render(request, 'rango/index.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = []

    return render(request, 'rango/category.html', context=context_dict)


def about(request):
    print(request.method)
    print(request.user)
    return render(request, 'rango/about.html', {})


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            context_dict = {'form': form, 'category': category, 'errors': form.errors}
            return render(request, 'rango/add_page.html', context=context_dict)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)
