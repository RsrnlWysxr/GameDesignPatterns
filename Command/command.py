# -*- encoding: utf-8 -*-
'''
简单实现
'''


def press(input):
    print input


def jump_action():
    print "jump"


def fire_gun_action():
    print "fire gun"


def swap_weapon_action():
    print "swap weapon"


def reload_bullet_action():
    print "reload"


def Input():
    if press('x'):
        jump_action()
    elif press('y'):
        fire_gun_action()
    elif press('a'):
        swap_weapon_action()
    elif press('b'):
        reload_bullet_action()


'''
配置按键
个人思路:
将变量和函数对象绑定
'''


class PressAction(object):
    INSTANCE = {}

    def __init__(self, press, action):
        self.press = press
        self.action = action
        self.INSTANCE[self.press] = self

    def reset_press(self, new_press):
        self.INSTANCE.pop(self.press)
        self.press = new_press
        self.INSTANCE[self.press] = self

    def execute(self):
        self.action()


'''
全局初始化
'''

jump = PressAction('x', jump_action)
fire_gun = PressAction('y', fire_gun_action)
swap_weapon = PressAction('a', swap_weapon_action)
reload_bullet = PressAction('b', reload_bullet_action)


class InputHander(object):
    def __init__(self):
        self.press_actions = PressAction.INSTANCE

    def input(self):
        press_action = self.press_actions.get()
        if press_action:
            press_action.execute()
