from __future__ import unicode_literals

from django.db import migrations, models


def add_test_devices(apps, schema_editor):
    PhysicalDevice = apps.get_model('core', 'PhysicalDevice')
    LogicalDevice = apps.get_model('core', 'LogicalDevice')

    pd1 = PhysicalDevice(device_id='my-first-device')
    pd1.save()
    ld1 = LogicalDevice(
        physical_device=pd1,
        device_id='Device1',
        connected=False,
        device_name='',
        device_type='switch',
        device_status='OFF'
    )
    ld1.save()
    ld2 = LogicalDevice(
        physical_device=pd1,
        device_id='Device2',
        connected=True,
        device_name='Switch 1',
        device_type='switch',
        device_status='OFF'
    )
    ld2.save()

    pd2 = PhysicalDevice(device_id='my-second-device')
    pd2.save()
    ld3 = LogicalDevice(
        physical_device=pd2,
        device_id='Device1',
        connected=False,
        device_name='',
        device_type='switch',
        device_status='ON'
    )
    ld3.save()
    ld4 = LogicalDevice(
        physical_device=pd2,
        device_id='Device2',
        connected=True,
        device_name='Switch 2',
        device_type='switch',
        device_status='ON'
    )
    ld4.save()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_test_devices),
    ]
