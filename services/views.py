from django.shortcuts import render
from .models import ServiceProvider

def service_list(request):
    query = request.GET.get('q')
    if query:
        # Filter by service_type if query matches the service_type field
        services = ServiceProvider.objects.filter(service_type__icontains=query)
    else:
        # If no query, return all services
        services = ServiceProvider.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'services/service_list.html', context)

#from django.db.models import Q
#services = ServiceProvider.objects.filter(name__icontains=query)
#services = ServiceProvider.objects.all()