from django.db import models
from datetime import datetime

"""
Model Relation

Device -one-to-many-> Temperature -many-to-one-> Employee

1. One device can record many temperatures, but a temperature must only belong to one device (where it was recorded).
2. An employee can record their temperature multiple times, but a temperature can only belong to a single employee.

"""

# The device model representing the temperature reading device


class Device(models.Model):
    STATUS = (('Working', 'Working'), ('Broken', 'Broken'))

    # I have opted to not define a name for the device. It shall be identified
    # by its index. For example, Device 1

    # The device is either working or broken
    status = models.CharField(
        default='Working', max_length=10, null=True, choices=STATUS)

    # Example: Device 1
    def __str__(self):
        return "Device {}".format(self.id)

# The Employee model representing the employees in the company


class Employee(models.Model):

    # The name of the employee
    name = models.CharField(max_length=200)

    # Example: Ruthuparna
    def __str__(self):
        return self.name

# The temperature model representing body temperature


class Temperature(models.Model):

    # The body temperature of the employee in Farehneit
    temperature = models.IntegerField()

    # The datetime when the temperature was recorded. Current datetime as default.
    date = models.DateTimeField(default=datetime.now, null=True)

    # The reference to the device that recorded the temperature. If device is deleted, this reference becomes null
    # (makes sense to keep the temperature records even after the device is deleted)
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)

    # The reference to the employee that recorded the temperature. If employee is deleted, this reference is deleted
    # as well (no point in keeping the temperature of an employee who no longer exists)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    # Example: Ruthuparna - 100 at 2021-07-10 13:14:52.984238+00:00
    def __str__(self):
        return "{} - {} at {}".format(self.employee.name, self.temperature, self.date)
