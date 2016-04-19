from .models import *
from django.views.generic import ListView


class HomepageView(ListView):
    template_name = 'index.html'
    model = LogicalDevice
    queryset = LogicalDevice.objects.filter(connected=True)
    context_object_name = 'devices'


class DiscoveredView(ListView):
    template_name = 'discovered.html'
    model = PhysicalDevice
    #queryset = PhysicalDevice.objects.all()
    context_object_name = 'devices'


