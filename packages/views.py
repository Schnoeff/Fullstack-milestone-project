from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Package
# Create your views here.


def all_packages(request):
    """ returns all of the packages available """

    packages = Package.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                packages = packages.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            packages = packages.order_by(sortkey)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No suitable search requirements met!")
                return redirect(reverse('packages'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            packages = packages.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'packages': packages,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'packages/packages.html', context)
