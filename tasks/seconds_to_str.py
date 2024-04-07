import datetime

__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    
    days = seconds // (24 * 3600)
    hours = (seconds % (24 * 3600)) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    result = ""
    if days > 0:
        result += f"{days:02}d"
    if hours > 0 or days > 0:
        result += f"{hours:02}h"
    if minutes > 0 or hours > 0 or days > 0:
        result += f"{minutes:02}m"
    result += f"{seconds:02}s"

    return result