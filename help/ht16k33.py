from adafruit_ht16k33 import matrix

class matrix_helper:

    def __init__(self, matrix: matrix.Matrix8x8):
        self.__matrix = matrix

    def __transform(self, x, y) -> tuple[int, int]:
        if x > 0:
            x = 8 - x
        return (x, y)

    def pixel(self, x: int, y: int, c: bool | None):
        (x, y) = self.__transform(x, y)
        self.__matrix.pixel(x, y, c)
