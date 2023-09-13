import json
import time

with open('cs.json', encoding='utf-8') as my_file:
    quest = json.load(my_file)

greeting = f'''
Добро пожаловать в игру '{quest["game_info"]["name"]}'!
Авторы игры: {quest["game_info"]["author"]}
Версия игры: {quest["game_info"]["version"]}
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
    for action in quest["game"][scene]["ACTIONS"]:
        if "WHEN" in action:
            if "LACK" in action["WHEN"]:
                if action["WHEN"]["LACK"] not in inventory:
                    if "MISSED" in action["WHEN"]:
                        if action["WHEN"]["MISSED"] not in scenes:
                            print(' -> ', action["NAME"])
                    else:
                        print(' -> ', action["NAME"])
            elif "HAVE" in action["WHEN"]:
                if action["WHEN"]["HAVE"] in inventory:
                    print(' -> ', action["NAME"])
        else:
            print(' -> ', action["NAME"])


def get_user_action():
    while True:
        user_in = input()
        if user_in:
            return user_in


def check_action(scene, action_name):
    for allowed_action in quest["game"][scene]["ACTIONS"]:
        if allowed_action["NAME"] == action_name:
            return allowed_action["EFFECT"]


def perform_action(effect):
    global current_scene, quest, inventory, scenes
    if current_scene == 'SCENE_0':
        index = 1
    else:
        index = 2
    if "ALERT" in effect:
        if quest["game"][current_scene]["ACTIONS"][index]["WHEN"]:
            when_option = quest["game"][current_scene]["ACTIONS"][index]["WHEN"]
            if "LACK" in when_option:
                item_found = False

                for i in range(len(inventory)):
                    if inventory[i] == when_option["LACK"]:
                        item_found = True
                        break

                if item_found is False:
                    print(effect["ALERT"])
                    if "COLLECT" in when_option:
                        inventory.append(effect["COLLECT"])

            if "HAVE" in when_option:
                for i in range(len(inventory)):  # Можно было записать без цикла for, а через условие in
                    if inventory[i] == when_option["HAVE"]:
                        print(effect["ALERT"])
                        break
                if "DISPOSE" in effect:
                    inventory.remove(effect["DISPOSE"])

    if "GO" in effect:
        current_scene = effect["GO"]
        scenes.append(effect["GO"])


scenes = []
inventory = []
current_scene = 'respawn'

while True:
    time.sleep(3)
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