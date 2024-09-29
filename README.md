# Petstore API CRUD Test Suite

This project contains automated tests that follow the CRUD (Create, Read, Update, Delete) cycle for the Pet endpoint group of the Petstore Sample API. The tests are implemented using Python, pytest, and the requests library.

## Overview

The test suite covers the following operations:
- Create: Adding a new pet
- Read: Retrieving pet details
- Update: Modifying pet information
- Delete: Removing a pet

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository:

git clone ```https://github.com/rojekmac/Pet-store-sample-API```
cd petstore-api-tests


2. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate


3. Install the required packages:

```pip install requests pytest pytest-html```


## Running the Tests

To run the tests, execute the following command in the project root directory:

pytest test_pet_crud_operations.py

For a more detailed output, use:

pytest -v test_pet_crud_operations.py


## Test Structure

The test file `test_pet_crud_operations.py` contains:
- Fixtures for creating test data and adding a new pet
- Individual test functions for each CRUD operation
- Assertions to verify the expected behavior of the API

## API Documentation

For more details about the Petstore Sample API, refer to the [official documentation](https://petstoresampleapi.apimatic.dev/).

## Contributing

Contributions to improve the test suite are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request

## License

This project is licensed under the **"Don't Steal My Code" License**. You can use it, modify it, and share it, but if you make millions off it, at least buy me a coffee (or a pizza, I’m not picky). 

Just remember: with great power comes great responsibility. Use wisely and don't break the internet!
