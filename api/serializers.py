from rest_framework import serializers
from .models import Device, Temperature, Employee

# Serializers are used to convert the complex query objects obtained from the db into simpler native python datastructures for the response


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
