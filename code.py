import board
import busio
import time
from adafruit_ht16k33 import matrix
from help.ht16k33 import matrix_helper

with busio.I2C(board.SCL, board.SDA) as i2c:

    matrix = matrix.Matrix8x8(i2c, brightness=0.1)

    mt_helper = matrix_helper(matrix)

    matrix.fill(0)

    for y in range(8):
        for x in range(8):
            mt_helper.pixel(x, y, 1)
            #matrix[x, y] = 1
            #matrix.show()
            time.sleep(0.1)
