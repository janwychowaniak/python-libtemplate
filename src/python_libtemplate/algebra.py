from typing import Tuple, Union
from loguru import logger

from .arithmetic import subtract
from .exceptions import NoRealSolutionError


def quadratic_formula(a: float, b: float, c: float) -> Tuple[float, float]:
    """
    Solves a quadratic equation in the form ax^2 + bx + c = 0.
    Returns the two possible solutions as (x1, x2).
    """
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        # Logging the error condition before raising the exception
        logger.error(f"The equation ax^2 + bx + c = 0 with a={a}, b={b}, c={c} has no real solutions.")
        raise NoRealSolutionError("The quadratic equation has no real solution.")

    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    return x1, x2


def solve_linear_equation(a: float, b: float) -> Union[float, str]:
    """
    Solve the equation ax + b = 0 for x.

    NOTE: the function is supposed to demonstrate
          same-level modules interdependence.
    """
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    return subtract(0, b) / a
