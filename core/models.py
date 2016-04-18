from django.db import models

class PhysicalDevice(models.Model):
    device_id = models.CharField(max_length=50, unique=True)

class LogicalDevice(models.Model):
    physical_device = models.ForeignKey(PhysicalDevice, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=50)
    connected = models.BooleanField(default=False)
    device_name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=30)
    device_status = models.TextField()
