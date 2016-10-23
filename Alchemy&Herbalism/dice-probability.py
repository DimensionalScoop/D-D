import os

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

sample_size = 1000000

dice_range = 4 + 6 + 8
dice_rolls = [0.] * (dice_range + 1)

tripplets = 0.
doubles = 0.


def d(faces):
    return np.random.randint(1, faces + 1)


def dice_roller():
    return d(4) + d(6) + d(8)  # 2d6+1d4

for i in range(sample_size):
    dice_rolls[dice_roller()] += 1
    a = d(4)
    b = d(6)
    c = d(8)
    if a == b and b == c:
        tripplets += 1
    else:
        if a == b:
            doubles += 1
        if b == c:
            doubles += 1
        if a == c:
            doubles += 1

for i in range(dice_range + 1):
    dice_rolls[i] /= sample_size

plt.plot(range(dice_range + 1), dice_rolls, "r.")

for i in range(dice_range + 1):
    print(i, "at", dice_rolls[i] * 100, "%")

print("Doubles:", doubles / sample_size)
print("Tripplets:", tripplets / sample_size)

plt.show()
