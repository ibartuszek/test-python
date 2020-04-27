import pyautogui

# Screen size
top_position = 570
bottom_position = 1040
left_position = 0
right_position = 830
# 830
width = right_position - left_position
# 470
height = bottom_position - top_position

# y --> 750
intel_x = width * 0.74 + left_position
intel_y = height * 0.38 + top_position
money_x = width * 0.58 + left_position
money_y = intel_y
weapon_smith_x = money_x
weapon_smith_y = height * 0.54 + top_position
elite_training_room_x = intel_x
elite_training_room_y = weapon_smith_y
training_room_1_x = money_x
training_room_1_y = height * 0.71 + top_position
training_room_2_x = intel_x
training_room_2_x = training_room_1_y

# Right Traning room coord: 610 / 910


def collect_money():
    pyautogui.moveTo(money_x, money_y)
    pyautogui.click()


def collect_intel():
    pyautogui.moveTo(intel_x, intel_y)
    pyautogui.click()
    # TODO:
    # pyautogui.sleep(1)
    # ok_popup = pyautogui.locateOnScreen('ok.png')
    # pyautogui.sleep(2)
    # print(ok_popup)
    # if (ok_popup != none)


# TODO:
def train_one():
    pyautogui.moveTo(weapon_smith_x, weapon_smith_y)
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.sleep(1)
    pyautogui.scroll(1, 0, 1)


# Test
screenWidth, screenHeight = pyautogui.size()
print("width: {0}; height: {0}".format(screenWidth, screenHeight))
# pyautogui.sleep(1)
# collect_money()
# pyautogui.sleep(1)
# collect_intel()
# pyautogui.doubleClick()



