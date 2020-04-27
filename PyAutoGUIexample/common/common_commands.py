import pyautogui

# in case of my laptop
# top_position = 360
# bottom_position = 820
# factor = 1.25

# in case of my PC
top_position = 575
bottom_position = 1040
factor = 1.0

left_position = 0
right_position = 830

# 830
width = right_position - left_position
# 470
height = bottom_position - top_position


def click_cursor_on(x, y):
    pyautogui.moveTo((x + left_position) * factor, (y + top_position) * factor)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(2)
