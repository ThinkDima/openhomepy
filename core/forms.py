from django import forms
from .models import LogicalDevice

class ConnectForm(forms.ModelForm):
    class Meta:
        model = LogicalDevice
        exclude = ['device_status', 'connected', 'physical_device']

    def __init__(self, *args, **kwargs):
        super(ConnectForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['device_id'].widget.attrs['readonly'] = True
            self.fields['device_type'].widget.attrs['readonly'] = True
            self.fields['device_name'].widget.attrs['autofocus'] = True
            self.fields['device_name'].widget.attrs['class'] = 'form-control'
