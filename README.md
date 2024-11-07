# dsss_homework_2
Homework 02 - Data Science Survival Skills WS2024/25 FAU

# Math Quiz Game

This game is an assignment for Data Science Survival Skills WS2024/25 at FAU. This game generates random math question that includes addition, subtraction and multiplication with random numbers. 

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Functions](#functions)
- [Examples](#examples)
- [Testing](#testing)
- [License](#license)


## Installation

To install the `math_quiz` package, you can use `pip`. Please check the all requirements from the `requirements.txt` file.

In order to install the package, you can use the following command:

```bash
pip install git+https://github.com/mrfbgc/dsss_homework_2.git
```

### Requirements

In this python project, python 3.12.4 version is used.

It is required to use `setuptools>=58.0.0` in this project. 

In order to install the all requirements, please run the following command.

```bash
pip install -r requirements.txt
```

## Functions

You can import and use `math_quiz` functions in your Python code. The main functions provided by the package include:

- `random_number_generator(min, max)`: Generates a random number between `min` and `max`.
- `random_operation_selector()`: Randomly selects an operation (`+`, `-`, `*`) for the quiz.
- `question_generator(num1, num2, op)`: Generates a math problem and calculates the answer based on the provided numbers and operation.
- `math_quiz()`: Runs an interactive math quiz in the terminal.


## Examples

When you run the `math_quiz()` function, you will be prompted with questions like:

```plaintext
Welcome to the math quiz! Let's get started.
What is 5 + 3? 
> 8
Correct! Next question.
```

## Testing

This package includes unit tests for the main functions. To run the tests, navigate to the `math_quiz` directory and run:

```bash
python -m unittest tests_math_quiz.py
```


## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or need further assistance, feel free to reach out to:

- **Author**: Mehmet Arif Bagci
- **Email**: mehmet.a.bagci@fau.de


