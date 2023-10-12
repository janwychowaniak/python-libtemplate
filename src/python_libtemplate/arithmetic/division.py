from typing import Tuple
from loguru import logger


def divide(a: float, b: float) -> Tuple[float, float]:
    """Divides a by b. Returns a tuple (quotient, remainder)."""
    if b == 0:
        logger.error("Cannot divide by zero.")
        raise ValueError("Cannot divide by zero.")
    quotient = a // b
    remainder = a % b
    return quotient, remainder
