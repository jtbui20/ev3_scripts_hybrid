from typing import Tuple, List


def AddMatrix(A: List[float], B: List[float]) -> List[float]:
    return [A[i] + B[i] for i in range(0, len(A))]


def AngleBetween(current: int, target: int) -> Tuple[float, int]:
    """Gets the difference between two directions"""
    angle_dif = ((current - target + 180) % 360) - 180
    direction = 1 if (angle_dif > 0) else -1
    return (abs(angle_dif), direction)
