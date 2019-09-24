# -*- encoding: utf-8 -*-
'''
简单实现
'''


def jump_action():
    print "jump"


def fire_gun_action():
    print "fire gun"


def swap_weapon_action():
    print "swap weapon"


def reload_bullet_action():
    print "reload"


def normal_input(key):
    if key == 'x':
        jump_action()
    elif key == 'y':
        fire_gun_action()
    elif key == 'a':
        swap_weapon_action()
    elif key == 'b':
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

jump.reset_press('j')
fire_gun.reset_press('r')
swap_weapon.reset_press('s')
reload_bullet.reset_press('b')


class InputHander(object):
    def __init__(self):
        self.press_actions = PressAction.INSTANCE

    def advance_input(self, key):
        press_action = self.press_actions.get(key)
        if press_action:
            press_action.execute()


def main():
    down_key = raw_input("Down key: ")
    input_hander = InputHander()
    input_hander.advance_input(down_key)


if __name__ == "__main__":
    while True:
        main()
