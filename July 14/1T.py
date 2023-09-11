import json
import time

with open('kolobok.json', 'r', encoding='utf-8') as my_file:
    quest = json.load(my_file)

greeting = f'''
Добро пожаловать в игру '{quest["game_info"]["NAME"]}'!
Авторы игры: {quest["game_info"]["AUTHOR"]}
Версия игры: {quest["game_info"]["VERSION"]}
'''

print(greeting)


def show_description(scene):
    description = quest["game"][scene]["DESCRIPTION"]
    print(description)


def is_game_end(scene):
    if "ACTIONS" in quest["game"][scene]:
        return False
    return True


def show_actions(scene):
    print('Что будете делать?')
    for current_action in quest["game"][scene]["ACTIONS"]:
        print(' -> ', current_action["NAME"])


def get_user_action():
    while True:
        user_in = input()
        if user_in:
            return user_in


def check_action(scene, action_name):
    for allowed_action in quest["game"][scene]["ACTIONS"]:
        if allowed_action["NAME"] == action_name:
            return allowed_action["EFFECT"]
        if "WHEN" in allowed_action and allowed_action["WHEN"] in quest["game"][scene]["ACTIONS"]:
            if allowed_action["WHEN"]["LACK"] and allowed_action["WHEN"]["MISSED"]:
                print(allowed_action["EFFECT"]["ALERT"])
                global inventory
                inventory.append(allowed_action["EFFECT"]["COLLECT"])
                allowed_action["EFFECT"]
                get_user_action()
                return
# разобраться с 'when'
# тут надо поделить лак и миссед
# тут менять надо


def perform_action(current_effect):
    global current_scene
    current_scene = current_effect["GO"]


inventory = []
current_scene = 'SCENE_0'


while True:
    print(f'\n{"-" * 50} \n')
    show_description(current_scene)
    if is_game_end(current_scene):
        break
    show_actions(current_scene)
    action = get_user_action()
    effect = check_action(current_scene, action)
    if effect:
        perform_action(effect)
    else:
        print('Такого действия нету. Выберите другое')