def ClampSpeed(values, speed=100):
    """Changes the highest motor speed to the speed specified while maintaining the ratio of the other motors"""
    high = max([abs(x) for x in values])
    if high == 0:
        return values
    ratio = speed / high
    return [min(100, max(-100, ratio * x)) for x in values]
