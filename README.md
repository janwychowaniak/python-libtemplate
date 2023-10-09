# python-libtemplate - A Template for Python Libraries

`python-libtemplate` serves as an example and template for those looking to create their own Python libraries. This project showcases standard practices, modular design, error handling, and unit testing. While it offers basic mathematical functionalities as its core feature, the main purpose is to **demonstrate how to structure and document a Python library effectively**.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [For Development](#installation-for-development)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Algebraic solutions: solving linear and quadratic equations.
- Custom exception handling for specific error scenarios.
- Comprehensive unit tests using `pytest`.

## Installation

To install `python-libtemplate`, navigate to its directory and run:

```bash
pip install .
```

### Installation for Development

To set up the library for development:

1. Clone the repository.
2. Navigate to its directory.
3. Install the main dependencies:

```bash
pip install -r requirements.txt
```

4. For additional development tools and dependencies:

```bash
pip install -r requirements-dev.txt
```

## Usage

Here's a quick start to using the library:

```python
from python_libtemplate import arithmetic, algebra

# Basic arithmetic
print(arithmetic.add(2, 3))  # Output: 5

# Algebraic solutions
print(algebra.quadratic_formula(1, -3, 2))  # Outputs: (2.0, 1.0)
print(algebra.solve_linear_equation(1, -3))  # Output: 3.0
```

## Testing

To ensure the reliability of the library, comprehensive tests have been written using `pytest`. To run these tests, simply execute:

```bash
pytest
```

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. If you have any questions, please open an issue.

## License

MIT.
