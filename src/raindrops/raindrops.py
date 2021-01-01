"""
raindrops implements a function for converting numbers to raindrop sounds based
on modulo arithmetic.
"""


def convert(number):
    """
    convert a number into a string that contains raindrop sounds corresponding
    to certain potential factors. A factor is a number that evenly divides into
    another number, leaving no remainder.

    Example:
    >>> convert(3)
    'Pling'
    >>> convert(15)
    'PlingPlang'
    >>> convert(23)
    '23'
    """
    raindrops = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    result = "".join(sound for divisor, sound in raindrops if number % divisor == 0)
    if result:
        return result
    return str(number)
