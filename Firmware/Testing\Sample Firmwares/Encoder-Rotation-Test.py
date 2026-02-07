import board
import digitalio
import time

a = digitalio.DigitalInOut(board.D3)
b = digitalio.DigitalInOut(board.D8)

a.pull = digitalio.Pull.UP
b.pull = digitalio.Pull.UP

while True:
    print(a.value, b.value)
    print("Haunted is my nigga")
    time.sleep(1)
