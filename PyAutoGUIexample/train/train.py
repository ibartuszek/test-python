import pyautogui

from PyAutoGUIexample.common.common_commands import click_cursor_on


# from common_commands import click_cursor_on


def train_loop(limit, sleep, extra_codex):
    i = 0
    while i < limit:
        print("{0} iteration has started.".format(i))
        train_iteration(sleep, extra_codex)
        i += 1


def train_iteration(sleep, extra_codex):
    click_cursor_on(175, 410)
    click_cursor_on(115, 150)
    click_cursor_on(325, 310)
    # loop if you need extra codex
    get_extra_codex(extra_codex)
    click_cursor_on(740, 440)
    # pyautogui.sleep(sleep)
    # click_cursor_on(175, 410)
    # click_cursor_on(220, 345)
    # click_cursor_on(490, 270)
    # click_cursor_on(750, 430)


def get_extra_codex(extra_codex):
    counter = 1
    while counter <= extra_codex:
        click_cursor_on(390, 390)


# Test
print("Start training:")
train_loop(1, 1, 4)
print("Training has finished")
