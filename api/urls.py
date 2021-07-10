from django.urls import path
from . import views

urlpatterns = [

    # Index - provides a list of all the api routes
    path('', views.index, name="index"),

    # View - gets a list of the objects

    # Gets a list of all the devices
    path('device/', views.device, name="device"),
    # Gets the device for the given id
    path('device/<int:pk>/', views.device, name="device"),

    # Gets a list of all the temperatures
    path('temperature/', views.temperature,
         name="temperature"),
    # Gets the temperature for the given id
    path('temperature/<int:pk>/', views.temperature),

    # Gets a list of all the employees
    path('employee/', views.employee, name="employee"),
    # Gets the employee for the given id
    path('employee/<int:pk>/', views.employee, name="employee"),

    # Create objects of the models

    # Create a device
    path('device-create/', views.deviceCreate, name="device-create"),
    # Create a temperature
    path('temperature-create/', views.temperatureCreate,
         name="temperature-create"),
    # Create an employee
    path('employee-create/', views.employeeCreate, name="employee-create"),

    # Employee temperature - Get temperatures for an employee and date range
    path('employee-temperature/', views.employeeTemperature,
         name="employee-temperature"),

    # Employee Temperature More Than Hundred - Get employees with greater than
    # 100 temperature for a date
    path('employee-temperature-100/', views.employeeTemperatureMoreThanHundred,
         name="employee-temperature-100")

]
