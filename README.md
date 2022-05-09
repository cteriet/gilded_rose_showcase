# Gilded Rose Kata

## Installation/setup
Create/activate a Python 3.10 environment of choice. 

### Step 1: Install development dependencies
To run tests using pytest, mypy and flake8, install those libraries:

``
py -m pip install -r .\requirements_dev.txt
``

### Step 2: Install the production dependencies

The dependencies in requirements.txt aren't used for anyhting, but the requests 
library is listed as a (fictional) dependency for the GildedRose package, so we need it for that reason

``py -m pip install -r .\requirements.txt``

### Step 3: Install the GildedRose package

``pip install -e .``

## Running Tests
To run pytest and run all tests, do:

````aidl
pytest --cov-report term-missing
mypy src
flake8 src
````


## Running a simulation/exploratory test
To output a simulation of N days of the Gilded Rose inventory, do:

``py .\test\texttest_fixture.py``