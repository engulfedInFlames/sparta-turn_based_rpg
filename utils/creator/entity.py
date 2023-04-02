import random


class Entity:
    def __init__(self, name: str, hp: int, mp: int, str_: int, int_: int, dex_: int) -> None:
        self._name = name

        self._hp = hp
        self._mp = mp
        self._str = str_
        self._int = int_
        self._dex = dex_
        self._is_alive = True

        self._max_hp = hp
        self._max_mp = mp

        self._critical_rate = 10 + \
            round((self._str + self._int*0.5 + self._dex*5)/5)
        self._evasion_rate = 5 + round((self._str * 0.5 + self._dex*5) / 5)

        # 공격 데이터를 반환하는 공격 메소드
    def attack(self) -> list:
        # attack_info = [is_area_attack, damage]를 반환
        return []

        # 공격 데이터를 인자로 받는 피격 메소드
    def attacked(self, attack_info: list) -> None:
        # 체력 잔여량을 보여주는 내부 함수
        def show_hp() -> None:
            print(f"{self._name}의 남은 체력 : {self._hp} ")

        p = random.random()
        if p < self._evasion_rate:
            print(f"{self._name}이(가) 공격을 회피했습니다.")
            show_hp()
        else:
            print(f"{self._name}이(가) {attack_info[1]}의 피해를 입었습니다.")
            show_hp()

        # 내부 변수의 값을 변경하는 메소드

    def change_status(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f"_{key}", value)

        # 내부 변수의 값을 반환하는 메소드
    def get_status(self, *args) -> dict:
        attr_dict = {attr: getattr(self, f"_{attr}") for attr in args}
        return attr_dict
