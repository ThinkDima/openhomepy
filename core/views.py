from .models import *
from django.views.generic import ListView


class HomepageView(ListView):
    template_name='index.html'
    model = LogicalDevice
    queryset = LogicalDevice.objects.filter(connected=True)
    context_object_name = 'device'


class ConnectView(ListView):
    template_name='connect.html'
    model = LogicalDevice
    queryset = LogicalDevice.objects.filter(connected=False)
    context_object_name = 'device'
