# built-in
import sys
import os
import random

# customized
from utils.validation import *
from entity import Entity


def get_direct_dir_path(round: int) -> str:
    current_dir = os.path.abspath(os.path.dirname(__file__))

    for _ in range(round):
        current_dir = os.path.dirname(current_dir)

    return current_dir


utils_dir_path = get_direct_dir_path(1)
sys.path.append(utils_dir_path)


class Monster(Entity):
    def __init__(self, name: str, hp: int, mp: int, str_: int, int_: int, dex_: int, rank: int, skill: str = ""):
        super().__init__(name, hp, mp, str_, int_, dex_)
        self._rank = rank
        self._skill = skill
        self._current_hp = rank * 75

        normal_attack_random_value = random.randint(-2, 6)
        special_attack_random_value = random.randint(-4, 8)

        self.actions = {
            "1": {"verbose": "", "is_area_attack": False, "damage": rank*10 + normal_attack_random_value},
            "2": {"verbose": skill, "is_""is_area_attack": False, "damage": rank*20 + special_attack_random_value}
        }

    def show_skill(self):
        print(f"[{self._name}]몬스터가 [{self._skill}] 스킬을 사용했습니다.")

    def show_status(self):
        print(f"{self._name}의 상태\nHP {self._current_hp}")

# # 공격 받았을 때 쓰는 함수    <-캐릭터 클래스에 정의되어 있는데
#     def attacked(self, attack_info: list):
#         # attack_info = (is_attacked, damage)
#         if attack_info[0]:
#             print(
#                 f"{self._name}이(가) {attack_info[1]}의 데미지를 입었습니다.")
#             self.change_hp(attack_info[1])

#         else:
#             print(f"{self._name}이(가) 공격을 회피했습니다.")
#             self.change_hp()

    # 몬스터가 플레이어한테 일반 공격할 때 들어가는 함수
    # ❌ def attack(self):
    # ❌    return super().attack()

    def change_status(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f"_{key}", value)

    def get_status(self, *args):
        return [getattr(self, f"_{arg}") for arg in args]


dict_monster_rank1 = {
    "1": Monster("좀비", 1, "저주"), "2": Monster("구울", 1, "광신"), "3": Monster("황혼의 유령", 1, "축복받은 조준"),
    "4": Monster("가시 마귀", 1, "가시폭풍"), "5": Monster("가시 야수", 1, "서슬퍼런 칼날"), "6": Monster("서슬 가시", 1, "위세"),
    "7": Monster("가시 박쥐", 1, "맹공"), "8": Monster("어둠의 사냥꾼", 1, "암흑 화살")
}
dict_monster_rank2 = {
    "1": Monster("미라", 2, "암흑 최면"), "2": Monster("발굴된 시체", 2, "독"), "3": Monster("망자", 2, "암흑 주술"),
    "4": Monster("카데바", 2, "감염"), "5": Monster("지네", 2, "근접"), "6": Monster("모래 구더기", 2, "스톤 스킨")
}
dict_monster_rank3 = {
    "1": Monster("거대 거미", 3, "멀티플 샷"), "2": Monster("저승 꼭두각시", 3, "순간 이동"), "3": Monster("황혼의 영혼", 3, "암흑 혼령")
}
