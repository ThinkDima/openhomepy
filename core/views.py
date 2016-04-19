from .models import *
from .forms import *
from django.views.generic import ListView, FormView, UpdateView
from django.core.urlresolvers import reverse_lazy


class HomepageView(ListView):
    template_name = 'index.html'
    model = LogicalDevice
    queryset = LogicalDevice.objects.filter(connected=True)
    context_object_name = 'devices'


class DiscoveredView(ListView):
    template_name = 'discovered.html'
    model = PhysicalDevice
    context_object_name = 'devices'


class ConnectView(UpdateView):
    template_name = 'connect.html'
    model = LogicalDevice
    success_url = reverse_lazy('dashboard')
    fields = ['device_name']
