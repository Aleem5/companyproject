# Company Project REST API

    db.sqlite3 contains sample records
    query.sql contains the MySQL query for both DDL and query

## REST API 

    Rest API was created for the Employee Schema

    Schema present in `department.models.py` file

#### Admin Page
    - http://127.0.0.1:8000/admin/
    
    - super User credentials to access the django admin page
        username: admin
        pass    : admin123

#### Django setup and test commands
    $ python -m pip install poetry
    
    Navigate to pyproject.toml location and install/activate poetry virtual environment
    $ cd companyproject
    $ python -m poetry shell

    $ python -m pip install poetry
    $ poetry update
    
    $ cd company
    $ python manage.py runserver

    And, for testing, in another shell
    $ python manage.py test

    And, for curl based testing
    $ curl http://127.0.0.1:8000/employee/

### Endpoints

    GET http://127.0.0.1:8000/employee/

    Sample Response:
        `
        {
            "count": 4,
            "next": null,
            "previous": null,
            "results": [
                {
                    "emp_id": 1,
                    "name": "CEO",
                    "manager_name": null
                },
                {
                    "emp_id": 2,
                    "name": "A",
                    "manager_name": null
                },
                {
                    "emp_id": 3,
                    "name": "B",
                    "manager_name": null
                },
                {
                    "emp_id": 4,
                    "name": "C",
                    "manager_name": null
                }
            ]
        }
    `
