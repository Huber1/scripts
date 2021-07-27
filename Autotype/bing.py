import string
import pyautogui
import time
import random


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


time.sleep(3)

i = 0
while i < 30:
    randomString = get_random_string(5)
    pyautogui.hotkey('ctrl', 'l')  # ctrl-l to url field
    pyautogui.typewrite(randomString, interval=random.random() / 3)
    pyautogui.press('enter')  # press the Enter key
    time.sleep(random.random() * 3)
    if i % 5 == 0:
        time.sleep(random.random()+3)
    i = i + 1
