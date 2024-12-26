# Python calculate_average function bug
This repository demonstrates a common error in Python functions that handle numerical operations: the TypeError that arises when a list intended for numerical calculations contains a string element.  The `calculate_average` function is designed to compute the average of a list of numbers, but it fails gracefully when encountering an unexpected data type (a string in this case).

The `bug.py` file contains the buggy function, highlighting the error.  The solution, provided in `bugSolution.py`, addresses this issue using type checking and exception handling to provide more robust functionality.

This example is useful for understanding basic debugging techniques in Python, and showcases the importance of defensive programming to prevent unexpected errors.