"""
This file contains all the view functions for the api paths.

VIEW FUNCTIONS:

    * index(): GET
    
    Handle listing the objects:
    * device(request, pk -optional): GET
    * temperature(request, pk -optional): GET
    * employee(request, pk -optional): GET

    Handle creation of the objects:
    * deviceCreate(request): POST
    * temperatureCreate(request): POST
    * employeeCreate(request): POST

    Get temperatures for an employee and date range
    * employeeTemperature(request): POST
    Get employees with greater than 100 temperature for a date
    * employeeTemperatureMoreThanHundred(request): POST
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

"""
This function provides all the api routes

Args:
    request: the request passed to the function
Returns:
    json: a list of the description and api routes
"""


@api_view(['GET'])
def index(request):

    api_urls = {
        'Get all Devices': '/device',
        'Get a particular Device': '/device/<id>',
        'Get all Temperatures': '/temperature',
        'Get a particular Temperatures': '/temperature/<id>',
        'Get all Employees': '/employee/',
        'Get a particular Employee': '/employee/<id>',
        'Create Device': '/device-create',
        'Create Temperature': '/temperture-create',
        'Create Employee': '/employee-create',
        'Get temperatures for an employee and date range': '/employee-temperature',
        'Get employees with greater than 100 temperature for a date': '/employee-temperature-100'
    }

    return Response(api_urls)


"""
This function lists all the devices/device

Args:
    request: the request passed to the function
    pk: (optional) the primary key (id) of the device. If pk isn't specified all devices
        are returned
Returns:
    json: a list of the devices/device
"""


@api_view(['GET'])
def device(request, pk=None):

    if pk is None:
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    else:
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        if pk > len(serializer.data):
            error = {"Index out of range"}
            return Response(data=error, status=400)
        return Response(serializer.data[pk-1])


"""
This function lists all the temperatures/temperature

Args:
    request: the request passed to the function
    pk: (optional) the primary key (id) of the temperature. If pk isn't specified all temperatures
        are returned
Returns:
    json: a list of the temperatures/temperature
"""


@api_view(['GET'])
def temperature(request, pk=None):

    if pk is None:
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)
    else:
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        if pk > len(serializer.data):
            error = {"Index out of range"}
            return Response(data=error, status=400)
        return Response(serializer.data[pk-1])


"""
This function lists all the employees/employee

Args:
    request: the request passed to the function
    pk: (optional) the primary key (id) of the employee. If pk isn't specified all employees
        are returned
Returns:
    json: a list of the employees/employee
"""


@api_view(['GET'])
def employee(request, pk=None):

    if pk is None:
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    else:
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        if pk > len(serializer.data):
            error = {"Index out of range"}
            return Response(data=error, status=400)
        return Response(serializer.data[pk-1])


"""
This function creates a device

Args:
    request: the request passed to the function. The body contains:
        - id: int, (optional) By default, will auto-increment to next available id
        - status: string, (optional) 'Working' (default value) or 'Broken'
    
Returns:
    json: the created device
"""


@ api_view(['POST'])
def deviceCreate(request):
    serializer = DeviceSerializer(data=request.data)

    # Insert the device if valid
    if serializer.is_valid():
        serializer.save()
    else:
        error = {"Invalid Data"}
        return Response(data=error, status=400)

    return Response(serializer.data)


"""
This function creates a temperature

Args:
    request: the request passed to the function. The body contains:
        - id: int, (optional) By default, will auto-increment to next available id
        - temperature: int, The recorded body temperature in Farenheit
        - date: datetime, (optional) By default, will take current datetime. Specifies
                the datetime when the temperature was recorded
        - device: Device, the id of the device
        - employee: Employee, the id of the employee
    
Returns:
    json: the created temperature
"""


@ api_view(['POST'])
def temperatureCreate(request):
    serializer = TemperatureSerializer(data=request.data)

    # Insert the temperature if valid
    if serializer.is_valid():
        serializer.save()
    else:
        error = {"Invalid Data"}
        return Response(data=error, status=400)

    return Response(serializer.data)


"""
This function creates a employee

Args:
    request: the request passed to the function. The body contains:
        - id: (optional) By default, will auto-increment to next available id
        - name: The name of the employee
    
Returns:
    json: the created employee
"""


@ api_view(['POST'])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)

    # Insert the employee if valid
    if serializer.is_valid():
        serializer.save()
    else:
        error = {"Invalid Data"}
        return Response(data=error, status=400)

    return Response(serializer.data)


"""
This function gets the temperatures for an employee and date range.
There are 4 possible scenarios:
    - start provided, end provided: return all temperatures of the employee within the range
    - start provided, end not provided: return all temperatures of the employee greater than or equal to start date
    - start not provided, end provided: return all temperatures of the employee lesser than or equal to end date
    - start not provided, end not provided: : return all temperatures of the employee

Args:
    request: the request passed to the function. The body contains:
        - employee: the id the employee
        - start: (optional) The start of the date range filter
        - end: (optional) The end of the date range filter
    
Returns:
    json: the list of temperatures based on the scenario
"""


@ api_view(['POST'])
def employeeTemperature(request):

    # The id of the employee to query
    try:
        employee = request.data["employee"]
    except:
        error = {"Please Provide employee"}
        return Response(data=error, status=400)

    # Check if start was passed, if not set it to None
    try:
        start = request.data["start"]
    except:
        start = None

    # Check if end was passed, if not set it to None
    try:
        end = request.data["end"]
    except:
        end = None

    # Query for the temperatures based on the scenario
    if start is not None:
        if end is not None:
            # Scenario 1
            temperatures = Temperature.objects.filter(
                employee=employee, date__gte=start, date__lte=end)
        else:
            # Scenario 2
            temperatures = Temperature.objects.filter(
                employee=employee, date__gte=start)
    else:
        if end is not None:
            # Scenario 3
            temperatures = Temperature.objects.filter(
                employee=employee, date__lte=end)
        else:
            # Scenario 4
            temperatures = Temperature.objects.filter(
                employee=employee)

    serializer = TemperatureSerializer(temperatures, many=True)
    return Response(serializer.data)


"""
This function gets employees with greater than 100F temperature for a given date
There are 2 possible scenarios:
    - date provided: return all employees who had more than 100F temperature on the given date
    - date not provided: return all employees who had more than 100F temperature

Args:
    request: the request passed to the function. The body contains:
        - date: (optional) the date filter
    
Returns:
    json: the list of employees based on the scenario
"""


@ api_view(['POST'])
def employeeTemperatureMoreThanHundred(request):

    # Check if date was passed, if not set it to None
    try:
        date = request.data["date"]
    except:
        date = None

    # Query for the employees based on the scenario
    # We find the distinct employees since an employee might be present multiple times
    # as a result of having their temperature taken multiple times on the given date
    if date is not None:
        # Scenario 1
        employees = Employee.objects.filter(
            temperature__temperature__gt=100, temperature__date__date=date).distinct()
    else:
        # Scenario 2
        employees = Employee.objects.filter(
            temperature__temperature__gt=100).distinct()

    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
