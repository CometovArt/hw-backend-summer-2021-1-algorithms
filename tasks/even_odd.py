__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    
    if not numbers:
        return False
    
    even_sum = 0
    odd_sum = 0
    
    for number in numbers:
        even_sum += number if number % 2 == 0 else 0 
        odd_sum += number if not number % 2 == 0 else 0 
        
    if not odd_sum:
        return False
            
    return even_sum / odd_sum