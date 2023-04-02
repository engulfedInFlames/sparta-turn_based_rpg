# build-in
import sys
import os
import random
from time import sleep

# customized
from utils.db import class_dict
from utils.validation import *
from entity import Entity


def get_direct_dir_path(round: int) -> str:
    current_dir = os.path.abspath(os.path.dirname(__file__))

    for _ in range(round):
        current_dir = os.path.dirname(current_dir)

    return current_dir


utils_dir_path = get_direct_dir_path(1)
sys.path.append(utils_dir_path)


class Player(Entity):
    def __init__(self, name: str, hp: int, mp: int, str_: int, int_: int, dex_: int) -> None:
        super().__init__(name, hp, mp, str_, int_, dex_)

        self._class = None
        self._level = 1
        self._exp = 0
        self._gold = 0

        self._exp_limit = 100 + self._level + 50

        normal_attack_random_value = random.randint(-2, 6)
        special_attack_random_value = random.randint(-4, 8)

        self.actions = {
            "1": {"verbose": "베기", "is_area_attack": False, "damage": round((self._str * 3 + self._dex)/2) + normal_attack_random_value},
            "2": {
                "1": {"verbose": "찌르기 (단일 대상 공격)", "is_area_attack": False, "damage": round((self._str * 6 + self._dex * 2)/2) + special_attack_random_value},
                "2": {"verbose": "휘두르기 (광역 공격)", "is_area_attack": True, "damage": round((self._str * 3 + self._dex)/2) + special_attack_random_value},
            },
        }

    def attack(self) -> list:
        print(f"플레이어의 공격 차례입니다.")
        sleep(1)

        print(f"공격 유형을 선택하세요.")
        answer = input("1. 일반 공격    2. 특수 공격\n: ")
        attack_type = check_string_number_answer(answer, 2)

        if attack_type == "2":
            actions = self.actions[attack_type]

            for key in actions:
                print(f"{key}. {actions[key]['verbose']} ", end="  ")
            answer = check_string_number_answer(input(": "), 2)

            print(f"{self._name}이(가) {actions[answer]['verbose']}을(를) 시도합니다.")
            damage = actions[answer]["damage"]
            is_area_attack = actions[answer]["is_area_attack"]

            return [is_area_attack, damage]

        verbose, is_area_attack, damage = self.actions[attack_type]
        print(f"{self._name}이(가) {verbose}을(를) 시도합니다.")

        return [is_area_attack, damage]

    def level_up(self):
        level_up_info = 5

        self._exp = 0
        self._level += 1

        self._max_hp += level_up_info * 5
        self._max_mp += level_up_info * 5
        self._current_mp = self._max_mp
        self._current_hp = self._max_hp
        self._str += 3
        self._dex += 2

        print(
            f"""
                *** Level UP! 현재 스텟 ***
                이름    : {self._name}
                경험치  : {self._exp}/{self._exp_limit}
                HP      : {self._current_hp}/{self._max_hp}
                MP      : {self._current_mp}/{self._max_mp}
                골드    : {self._gold}
                """)


def create_player():
    # 이름 입력
    unchecked_answer = input("플레이어의 이름을 입력하세요 : ")
    player_name = check_name(unchecked_answer)

    # 직업 선택
    print("\n직업 선택은 무시된다.")
    print("직업을 선택하세요.")
    for key in class_dict:
        print(f"{key}. {class_dict[key]}", end="  ")
    print("")
    unchecked_answer = input(": ")
    answer_range = len(class_dict)
    vaild_answer = check_string_number_answer(unchecked_answer, answer_range)
    player_class = class_dict[vaild_answer]

    #
    player_obj = Player(player_name, 100, 60, 5, 5, 5)
    print(
        f"""
    ==========플레이어가 생성되었습니다!========== 

    이름: {player_obj._name} / 직업: 모험가

    HP: {player_obj._max_hp} / MP: {player_obj._max_mp}
    
    STR: {player_obj._str} / INT: {player_obj._int} / DEX: {player_obj._dex}
    
    """)

    print("    특수 공격 : ", end="")
    special_attacks = player_obj.actions["2"]
    for key in special_attacks:
        print(special_attacks[key]['verbose'], end="  ")
    print("")
    return player_obj


player = create_player()
