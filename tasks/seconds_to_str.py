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
    day = seconds // 86400
    seconds = seconds % (24 * 3600)
    hour = (seconds // 3600) % 24
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if day == 0:
        if hour == 0:
            if minutes == 0:
                return "%02ds" % (seconds)
            return "%02dm%02ds" % (minutes, seconds)
        return "%02dh%02dm%02ds" % (hour, minutes, seconds)
    return "%02dd%02dh%02dm%02ds" % (day, hour, minutes, seconds)
    raise NotImplementedError

print(seconds_to_str(93600))
