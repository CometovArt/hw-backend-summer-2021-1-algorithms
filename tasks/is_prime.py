__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    
    if number < 2:
        return False
    
    for i in range(2, number):
        if (number / i) % 2 == 0:
            return False
        
    return True