
[![pipeline status](https://gitlab.com/peakbreaker/MockQuerPy/badges/master/pipeline.svg)](https://gitlab.com/peakbreaker/MockQuerPy/commits/master)
[![coverage report](https://gitlab.com/peakbreaker/MockQuerPy/badges/master/coverage.svg)](https://gitlab.com/peakbreaker/MockQuerPy/commits/master)

## MockQuerPy

This project implements a mocking library for quick and easy testing of google
bigquery based python projects

![bigquery](./bigquery.png)

### Getting started

Instructions on getting a local developement copy on your machine

#### Using the Lib in your project

**Basic use:**

1. `$ pip install mockquerpy`
2. Use either the context manager or decorator in your tests:

```python
from mockquerpy import MockQuerPy, mockquerpy_wrap

with MockQuerPy(TEST_DATA) as bigquery:
    print('bigquery inside here is a mockobject')

@mockquerpy_wrap
def test_my_bq_implementation(bigquery):
    print('bigquery inside here is a mockobject')
    MockQuerPy.set_test_data(MY_TEST_DATA)
```

See the project [documentation](#) for more // TODO

#### Developing the library

##### Prereq
- Python 3.7 or higher

##### Instructions

**Developing the library**:
1. Set up a python virtualenv `$ virtualenv venv && source venv/bin/activate`
2. Install the dependencies `$ pip install -r requirements.txt`

### Testing

Project is being tested using the pytest framework. This is also added to the
CI pipeline.

`$ pytest .`

### Deploying

Deployment is and should be handled by the CD pipeline to the project, but can
be done manually:
