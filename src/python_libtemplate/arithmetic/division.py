from loguru import logger


def divide(a, b):
    """Divides a by b. Returns a tuple (quotient, remainder)."""
    if b == 0:
        logger.error("Cannot divide by zero.")
        raise ValueError("Cannot divide by zero.")
    quotient = a // b
    remainder = a % b
    return quotient, remainder
