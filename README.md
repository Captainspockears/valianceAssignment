# Valiance Solutions Temperature API

NOTE: This document is best viewed in Markdown format

This is the solution to the assignment provided by Valiance Solutions. The assignment instructs to create Django models and build a REST API using them.

The API revolves around the recording of temperatures of employees in a company. It contains three models:

- Device (Temperature Reading Device)
- Temperature (Body Temperature Reading)
- Employee

It follows the relation Device -&gt; Temperature -&gt; Employee

## Setting up the projects

Kindly follow the following steps to set up the project and run the server:

- Install the dependencies: `pip install -r requirements.txt`
- Run the server: `python manage.py runserver.py`
- The server will be running on 'http://localhost:8000/'.

## Endpoints

The following endpoints are available:

### Project index and admin

- ### Welcome Page : `GET /`

  The welcome page of the REST API server.

  ```
  Welcome to Valiance Solution's Temperature API!
  ```

- ### API index Page : `GET /api`

  Provides a list of all the api routes

  ##### HTTP 200 OK

  ```
  {
      "Get all Devices": "/device",
      "Get a particular Device": "/device/<id>",
      "Get all Temperatures": "/temperature",
      "Get a particular Temperatures": "/temperature/<id>",
      "Get all Employees": "/employee/",
      "Get a particular Employee": "/employee/<id>",
      "Create Device": "/device-create",
      "Create Temperature": "/temperture-create",
      "Create Employee": "/employee-create",
      "Get temperatures for an employee and date range": "/employee-temperature",
      "Get employees with greater than 100 temperature for a date": "/employee-temperature-100"
  }
  ```

- ### Admin Page : `GET /admin`
  Provides access to admin functionalities.

### Model Viewing

- ### Device : `GET /api/device/<optional id>`

  Provides a list all the devices or device

  Examples:

  1. GET /api/device/

     ##### HTTP 200 OK

     ```
     [
     {
         "id": 1,
         "status": "Working"
     },
     {
         "id": 2,
         "status": "Working"
     },
     {
         "id": 3,
         "status": "Working"
     }
     ]
     ```

  2. GET /api/device/1

     ##### HTTP 200 OK

     ```
     {
     "id": 1,
     "status": "Working"
     }
     ```

  3. GET /api/device/10

     ##### HTTP 400 Bad Request

     ```
     [
     "Index out of range"
     ]
     ```

- ### Temperature : `GET /api/temperature/<optional id>`

  Provides a list all the temperatures or temperature

  Examples:

  1. GET /api/temperature/

     ##### HTTP 200 OK

     ```
     [
     {
     "id": 1,
     "temperature": 100,
     "date": "2021-07-10T06:45:16.006534Z",
     "device": 1,
     "employee": 1
     },
     {
     "id": 2,
     "temperature": 101,
     "date": "2021-07-10T06:45:30.270795Z",
     "device": 2,
     "employee": 1
     },
     {
     "id": 3,
     "temperature": 98,
     "date": "2021-07-10T06:46:14.458054Z",
     "device": 1,
     "employee": 2
     }

     ...

     ]
     ```

  2. GET /api/temperature/1

     ##### HTTP 200 OK

     ```
     {
     "id": 1,
     "temperature": 100,
     "date": "2021-07-10T06:45:16.006534Z",
     "device": 1,
     "employee": 1
     }
     ```

  3. GET /api/temperature/10

     ##### HTTP 400 Bad Request

     ```
     [
     "Index out of range"
     ]
     ```

- ### Employee : `GET /api/employee/<optional id>`

  Provides a list all the employees or employee

  Examples:

  1. GET /api/employee/

     ##### HTTP 200 OK

     ```
     [
     {
     "id": 1,
     "name": "Ruthuparna"
     },
     {
     "id": 2,
     "name": "Ritu"
     },
     {
     "id": 3,
     "name": "Suhruth"
     }

     ...

     ]
     ```

  2. GET /api/employee/1

     ##### HTTP 200 OK

     ```
     {
     "id": 1,
     "name": "Ruthuparna"
     }
     ```

  3. GET /api/employee/10

     ##### HTTP 400 Bad Request

     ```
     [
     "Index out of range"
     ]
     ```

### Model Creation - insert endpoints (Problem 1)

- ### Device : `POST /api/device-create`

  Creates a device and inserts it into the database.

  Parameters:

  - status: string, (optional) 'Working' (default value) or 'Broken'

  Examples:

  1. POST /api/device-create/

     ##### HTTP REQUEST BODY

     ```
     {
        "status": "Working"
     }
     ```

     ##### HTTP RESPONSE 200 OK

     ```
     {
         "id": 4,
         "status": "Working"
     }
     ```

  2. POST /api/device-create/

     ##### HTTP REQUEST BODY (Empty body)

     ```

     ```

     ##### HTTP RESPONSE 200 OK

     ```
     {
         "id": 4,
         "status": "Working"
     }
     ```

  3. GET /api/employee/10

     ##### HTTP REQUEST BODY

     ```
     {
        "status": "Valiance"
     }
     ```

     ##### HTTP RESPONSE 400 BAD REQUEST

     ```
     [
         "Invalid Data"
     ]
     ```

- ### Temperature : `GET /api/temperature-create`

  Creates a temperature and inserts it into the database.

  Parameters:

  - temperature: int, The recorded body temperature in Farenheit
  - date: datetime, (optional) By default, will take current datetime. Specifies
    the datetime when the temperature was recorded
  - device: (optional - recommended to provide or else device will be null) Device, the id of the device
  - employee: Employee, the id of the employee

  Examples:

  1. POST /api/device-create/

     ##### HTTP REQUEST BODY

     ```
     {
        "temperature": 100,
        "device": 1,
        "employee": 1
     }
     ```

     ##### HTTP RESPONSE 200 OK

     ```
     {
        "id": 8,
        "temperature": 100,
        "date": "2021-07-10T13:14:52.984238Z",
        "device": 1,
        "employee": 1
     }
     ```

  2. POST /api/device-create/

     ##### HTTP REQUEST BODY (No employee reference)

     ```
     {
        "temperature": 100
     }

     ```

     ##### HTTP RESPONSE 400 BAD REQUEST

     ```
     [
        "Invalid Data"
     ]
     ```

- ### Employee : `GET /api/employee-create`

  Creates an employee and inserts it into the database.

  Parameters:

  - name: The name of the employee

  Examples:

  1. POST /api/employee-create/

     ##### HTTP REQUEST BODY

     ```
     {
        "name":"Vignesh"
     }
     ```

     ##### HTTP RESPONSE 200 OK

     ```
     {
        "id": 5,
        "name": "Vignesh"
     }
     ```

  2. POST /api/employee-create/

     ##### HTTP REQUEST BODY (Empty Body)

     ```

     ```

     ##### HTTP RESPONSE 400 BAD REQUEST

     ```
     [
        "Invalid Data"
     ]
     ```

### Temperature Query `GET /api/employee-temperature` (Problem 2)

Gets all the temperatures recorded for a particular employee with date filters.
There are 4 possible scenarios:

- start provided, end provided: return all temperatures of the employee within the range
- start provided, end not provided: return all temperatures of the employee greater than or equal to start date
- start not provided, end provided: return all temperatures of the employee lesser than or equal to end date
- start not provided, end not provided: : return all temperatures of the employee

Parameters:

- employee: the id the employee
- start: (optional) The start of the date range filter
- end: (optional) The end of the date range filter

Examples:

1. POST /api/employee-temperature

   ##### HTTP REQUEST BODY (Scenario 1)

   ```
   {
      "employee": 1,
      "start": "2021-07-05",
      "end": "2021-07-07"
   }
   ```

   ##### HTTP RESPONSE 200 OK

   ```
   [
    {
        "id": 6,
        "temperature": 105,
        "date": "2021-07-05T07:27:01Z",
        "device": 1,
        "employee": 1
    }
   ]
   ```

2. POST /api/employee-temperature

   ##### HTTP REQUEST BODY (Scenario 2)

   ```
   {
      "employee": 1,
      "start": "2021-07-05"
   }
   ```

   ##### HTTP RESPONSE 200 OK

   ```
   [
    {
        "id": 1,
        "temperature": 100,
        "date": "2021-07-10T06:45:16.006534Z",
        "device": 1,
        "employee": 1
    },
    {
        "id": 2,
        "temperature": 101,
        "date": "2021-07-10T06:45:30.270795Z",
        "device": 2,
        "employee": 1
    },
    {
        "id": 6,
        "temperature": 105,
        "date": "2021-07-05T07:27:01Z",
        "device": 1,
        "employee": 1
    }
    ...

   ]
   ```

3. POST /api/employee-temperature

   ##### HTTP REQUEST BODY (Scenario 3)

   ```
   {
      "employee": 1,
      "end": "2021-07-07"
   }
   ```

   ##### HTTP RESPONSE 200 OK

   ```
   [
    {
        "id": 6,
        "temperature": 105,
        "date": "2021-07-05T07:27:01Z",
        "device": 1,
        "employee": 1
    }
   ]
   ```

4. POST /api/employee-temperature

   ##### HTTP REQUEST BODY (Scenario 4)

   ```
   {
      "employee": 1
   }
   ```

   ##### HTTP RESPONSE 200 OK

   ```
   [
    {
        "id": 1,
        "temperature": 100,
        "date": "2021-07-10T06:45:16.006534Z",
        "device": 1,
        "employee": 1
    },
    {
        "id": 2,
        "temperature": 101,
        "date": "2021-07-10T06:45:30.270795Z",
        "device": 2,
        "employee": 1
    },
    {
        "id": 6,
        "temperature": 105,
        "date": "2021-07-05T07:27:01Z",
        "device": 1,
        "employee": 1
    },

    ...

   ]
   ```

5. POST /api/employee-temperature

   ##### HTTP REQUEST BODY (Empty Body)

   ```

   ```

   ##### HTTP RESPONSE 200 OK

   ```
   [
     "Please Provide employee"
   ]
   ```

### Employee Query `GET /api/employee-temperature-100` (Problem 3)

Get all the employees whose temperatures were more than 100°F for a particular date.

There are 2 possible scenarios:

- date provided: return all employees who had more than 100F temperature on the given date
- date not provided: return all employees who had more than 100F temperature

Parameters:

- date: (optional) the date filter

Examples:

1. POST /api/employee-temperature-100

   ##### HTTP REQUEST BODY (Scenario 1)

   ```
   {
      "date": "2021-07-05"
   }
   ```

   ##### HTTP RESPONSE 200 OK

   ```
   [
    {
        "id": 1,
        "name": "Ruthuparna"
    },
    {
        "id": 4,
        "name": "Shashank"
    }
   ]
   ```

2. POST /api/employee-temperature

   ##### HTTP REQUEST BODY (Scenario 2 - Empty Body)

   ```

   ```

   ##### HTTP RESPONSE 200 OK

   ```
   [
    {
        "id": 1,
        "name": "Ruthuparna"
    },
    {
        "id": 3,
        "name": "Suhruth"
    },
    {
        "id": 4,
        "name": "Shashank"
    }
   ]
   ```

## Contact and Feedback

This assignment was submitted by Ruthuparna K.

```
Contact Number: 8867092264
Email: ruthuparna1998@gmail.com
```

Please reach out to me for any clarification or doubts.

In case of needing to login as an admin to the site to manage model objects, use the following credentials:

```
Username: admin
Password: admin
```

Thank you for taking the time to review my assignment and job application :)
