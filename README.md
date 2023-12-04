# PetStore API Tests

This repository contains automated tests for the PetStore API using the PyTest framework and Python requests library.

## Project Structure

- **tests/**: Contains test files.
- **src/**: Contains the source code of the project.
- **conftest.py**: Fixture file.
- **requirements.txt**: Dependencies file.
- **README.md**: Project documentation.

## How to Run

1. Clone this repository to your local machine.
2. Install Python and ensure it's added to your system's PATH.
3. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```
   
## Execute the tests by running:

```bash
pytest tests/test_petstore_api.py
```

## Test Data

- **pet_data**: A PyTest fixture providing sample data for Pet operations.
- **order_data**: A PyTest fixture providing sample data for Store operations.

## Cleaning Up

- Test data is automatically deleted after each test execution.

## Dependencies

- Python 3.x
- PyTest
- Requests
