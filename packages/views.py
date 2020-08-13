from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Package
# Create your views here.


def all_packages(request):
    """ returns all of the packages available """

    packages = Package.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No suitable search requirements met!")
                return redirect(reverse('packages'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            packages = packages.filter(queries)

    context = {
        'packages': packages,
        'search_term': query,
    }

    return render(request, 'packages/packages.html', context)
