from django import forms
from .models import LogicalDevice
from django.forms.utils import ErrorList

class ConnectForm(forms.ModelForm):
    class Meta:
        model = LogicalDevice
        exclude = ['device_status', 'connected', 'physical_device', 'device_id', 'device_type']

    def __init__(self, *args, **kwargs):
        super(ConnectForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['device_name'].widget.attrs['autofocus'] = True
            self.fields['device_name'].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(ConnectForm, self).clean()
        device_name = cleaned_data.get('device_name')
        if LogicalDevice.objects.filter(device_name__iexact=device_name).count() > 0:
            self._errors['device_name'] = ErrorList(['Name Already Exists!'])

        return cleaned_data
