"""
The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
"""


def format_duration(seconds):
    """
    Converts a duration in seconds to a human-readable format.

    Args:
    - seconds (int): The duration in seconds.

    Returns:
    - str: A human-readable representation of the duration.
    """
    if seconds == 0:
        return "now"

    # Define the time units in seconds
    time_units = [("year", 365 * 24 * 60 * 60),
                  ("day", 24 * 60 * 60),
                  ("hour", 60 * 60),
                  ("minute", 60),
                  ("second", 1)]

    result = []
    # Calculate the number of each time unit and add it to the result list
    for unit, unit_seconds in time_units:
        if seconds >= unit_seconds:
            # Calculate the number of units of the current time unit and add it to the result list
            # e.g. seconds = 3662, unit_seconds = 60*60 = 3600, count = 1
            # e.g. seconds = 62, unit_seconds = 365*24*60*60 = 31536000, count = 0
            count = seconds // unit_seconds
            # e.g. seconds = 62, unit_seconds = 365*24*60*60 = 31536000, count = 0, unit[:-1] = "year"
            result.append(f"{count} {unit}s" if count > 1 else f"{count} {unit}")
            # Update the remaining seconds after subtracting the number of units of the current time unit
            seconds %= unit_seconds

    # Join the formatted time units with commas and "and"
    formatted_duration = ", ".join(result[:-1]) + \
                         (" and " + result[-1] if len(result) > 1 else result[-1])

    return formatted_duration


# Example usage:
seconds_1 = 62
print(format_duration(seconds_1))  # Output: "1 minute and 2 seconds"

seconds_2 = 36625
print(format_duration(seconds_2))  # Output: "1 hour, 1 minute and 2 seconds"

seconds_3 = 31982000
print(format_duration(seconds_3))  # Output: "1 hour, 1 minute and 2 seconds"
