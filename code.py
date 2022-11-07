import board
import busio
import adafruit_ssd1306

i2c = busio.I2C(board.SCL, board.SDA)

display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

print("Text test")
display.fill(0)
char_width = 6
char_height = 8
chars_per_line = display.width // 6
for i in range(255):
    x = char_width * (i % chars_per_line)
    y = char_height * (i // chars_per_line)
    display.text(chr(i), x, y, 1)
display.show()

