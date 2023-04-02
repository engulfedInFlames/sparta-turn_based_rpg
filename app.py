import random
import sys
# 사용자 정의 모듈
from .utils.creator.player import create_player, Player
from .utils.creator.monster import Monster
from .utils.scripts.script import *

# intro()

player = create_player()

monster_dict = [
    {
        "1": Monster("좀비", 1, "저주"), "2": Monster("구울", 1, "광신"), "3": Monster("황혼의 유령", 1, "축복받은 조준"),
        "4": Monster("가시 마귀", 1, "가시폭풍"), "5": Monster("가시 야수", 1, "서슬퍼런 칼날"), "6": Monster("서슬 가시", 1, "위세"),
        "7": Monster("가시 박쥐", 1, "맹공"), "8": Monster("어둠의 사냥꾼", 1, "암흑 화살")
    },
    {
        "1": Monster("미라", 2, "암흑 최면"), "2": Monster("발굴된 시체", 2, "독"), "3": Monster("망자", 2, "암흑 주술"),
        "4": Monster("카데바", 2, "감염"), "5": Monster("지네", 2, "근접"), "6": Monster("모래 구더기", 2, "스톤 스킨")
    },
    {
        "1": Monster("거대 거미", 3, "멀티플 샷"), "2": Monster("저승 꼭두각시", 3, "순간 이동"), "3": Monster("황혼의 영혼", 3, "암흑 혼령")
    },
]

game_exit = False
first_town_visit = True

exp = 0
gold = 0
reward = [exp, gold]

is_clear_rank3 = False

while not game_exit:
    def in_town(player: Player, first_town_visit: bool):
        if first_town_visit:
            print("용사여! 마법의 세계 에테리아에 오신 것을 환영합니다.\n")
        else:
            print("...던전 탐색을 마치고 에테리아에 돌아왔다...\n")

        go_dungeon = False

        while not go_dungeon:
            dungeon_level = None
            answer_list = ["1", "2", "3"]

            print("1. 상점 방문 2. 던전 탐색 3. 내 스테이터스 확인")
            answer = input("어디로 향하시겠습니까? : ")

            while answer not in answer_list:
                answer = input("\n입력이 잘못됐습니다. 어디로 향하시겠습니까? : ")

            answer = int(answer)

            if answer == 1:
                print("\n상점을 방문했습니다.")
                print("\n상점에서 나왔습니다.")

            elif answer == 2:
                dungeon_level_list = ["1", "2", "3"]

                print("\n던전을 탐색합니다. 던전은 총 세 종류입니다.")
                print("1. 초급 던전 2. 중급 던전 3. 상급 던전 ")
                dungeon_level = input("어디로 향하시겠습니까? : ")

                while dungeon_level not in dungeon_level_list:
                    print("\n입력이 잘못됐습니다.")
                    print("던전은 총 세 종류입니다.")
                    print("1. 초급 던전 2. 중급 던전 3. 상급 던전 ")
                    dungeon_level = input("어디로 향하시겠습니까? : ")

                dungeon_level = int(dungeon_level)

                if dungeon_level == 1:
                    print("초급 던전으로 향합니다.")
                    dungeon_script_level1()

                elif dungeon_level == 2:
                    print("중급 던전으로 향합니다.")
                    dungeon_script_level2()

                else:
                    print("상급 던전으로 향합니다.")
                    dungeon_script_level3()

                go_dungeon = True

            else:
                [name, max_hp, current_hp, max_mp, current_mp, gold, exp_limit, exp] = player.get_status(
                    "name", "max_hp", "current_hp", "max_mp", "current_mp", "gold", "exp_limit", "exp")
                print(
                    f"""
                    *** 플레이어의 현재 상태 ***
                        이름    : {name}
                        경험치  : {exp}/{exp_limit}
                        HP      : {current_hp}/{max_hp}
                        MP      : {current_mp}/{max_mp}
                        골드    : {gold}
                    """)

        return dungeon_level

    dungeon_level = in_town(player, first_town_visit)
    first_town_visit = False

    # 1. 던전 진입
    is_in_dungeon = True
    while is_in_dungeon:

        temp_gold = 0
        temp_exp = 0

        # 2. 몬스터 생성
        def create_monster_list_with_name_list(_monster_dict: dict):
            def func(__monster_dict: dict, __monster_list: list, __monster_name_list: list, round: int):
                already_used_monster_number_list = []

                for _ in range(round):
                    length = len(__monster_dict)
                    monster_number = random.randint(1, length)

                    while monster_number in already_used_monster_number_list:
                        monster_number = random.randint(1, length)

                    already_used_monster_number_list.append(monster_number)
                    __monster_list.append(__monster_dict[str(monster_number)])
                    __monster_name_list.append(
                        __monster_dict[str(monster_number)].get_status("name")[0])

            _monster_list = []
            _monster_name_list = []

            p = random.random()
            if p < 0.4:
                func(_monster_dict, _monster_list, _monster_name_list, 1)

            elif p < 0.8:
                func(_monster_dict, _monster_list, _monster_name_list, 2)

            else:
                func(_monster_dict, _monster_list, _monster_name_list, 3)

            return _monster_list, _monster_name_list

        selected_monster_dict = monster_dict[dungeon_level - 1]
        monster_list, monster_name_list = create_monster_list_with_name_list(
            selected_monster_dict)

        monster_name_string = ""
        for i, monster_name in enumerate(monster_name_list):
            monster_name_string += f"{i+1}. {monster_name} "

        print("\n\n==================================================================")
        print("==================================================================")
        print("======================= 몬스터가 나타났다! =======================")
        print("==================================================================")
        print("==================================================================\n\n")

        print(f"{monster_name_string}", end="\n\n")

        # 3. 전투 여부 선택
        def is_battle_or_not():
            no_answer_check = False
            yes_answer_list = ["y", "yes"]
            no_answer_list = ["n", "no"]

            answer = input("전투하시겠습니까? (Y/N) : ").lower()

            while answer not in yes_answer_list:
                if answer in no_answer_list:
                    if not no_answer_check:
                        no_answer_check = True
                        answer = input("정말로 도망치시겠습니까? (Y/N) : ").lower()

                        if answer in yes_answer_list:
                            print("전투에서 비참하게 도망칩니다.\n")
                            return False

                        elif answer in no_answer_list:
                            break

                else:
                    if not no_answer_check:
                        answer = input(
                            "입력이 잘못됐습니다. 전투하시겠습니까? (Y/N) : ").lower()
                        print("")
                    else:
                        answer = input("입력이 잘못됐습니다. 정말로 도망치시겠습니까? (Y/N) : ")
                        print("")

                        if answer in yes_answer_list:
                            print("전투에서 비참하게 도망칩니다.\n")
                            return False

                        elif answer in no_answer_list:
                            break

            print("\n전투에 돌입합니다!")
            return True

        is_battle = is_battle_or_not()

        if not is_battle:
            is_in_dungeon = False

        # 4. 전투 돌입
        while is_battle:
            # 5. 플레이어가 공격
            # attack_info = [is_attack_success, is_area_attack, damage]
            attack_info = player.attack()

            # 6. 몬스터가 피격
            # 광역 공격일 때
            if attack_info[1]:
                for monster in monster_list:
                    if monster:
                        monster.attacked(attack_info)

            # 광역 공격 아닐 때
            else:
                def select_target(_monster_name_list: list):
                    target_list = []

                    for i, _monster_name in enumerate(_monster_name_list):
                        if _monster_name:
                            print(f"{i+1}. {_monster_name}", end=" ")
                            target_list.append(str(i+1))

                    print("")
                    target = input("목표를 선택하세요 : ")  # ✅✅✅ 몬스터 선택시 입력 유효성 검사

                    # 유효한 입력인지 확인
                    while target not in target_list:
                        target = input("입력이 잘못됐습니다. 목표를 선택하세요 : ")

                    target = int(target) - 1

                    return target

                target = select_target(monster_name_list)

                if monster_list[target]:
                    monster_list[target].attacked(attack_info)

            # 7. 몬스터 생사확인
            for i, monster in enumerate(monster_list):
                if monster_list[i]:
                    monster_is_alive = monster.get_status("is_alive")
                    if not monster_is_alive[0]:
                        print(f"{monster_name_list[i]}을(를) 무찔렀습니다!")

                        # 몬스터가 죽으면 list의 요소가 False가 됨.
                        monster_list[i] = False
                        monster_name_list[i] = False

                        # 보상 누적

                        exp = 30 + \
                            random.randint(0, 5) - (player._level - 1) * 10

                        gold = 10 + dungeon_level * 5 + random.randint(0, 10)

                        temp_exp += exp
                        temp_gold += gold

                        reward[0] += exp
                        reward[1] += gold

            if not any(monster_list):
                print("전투에서 승리했습니다.")
                # exp = reward[0]
                # gold = reward[1]

                player.change_status(exp=reward[0], gold=reward[1])

                print(
                    f"보상으로 {temp_gold} 골드와 {temp_exp} 경험치를 얻었습니다.", end="\n\n")

                if player._exp >= player._exp_limit:  # exp_limit달성 시 level_up함수 호출
                    player.level_up()

                if dungeon_level == 3 and not is_clear_rank3:
                    is_clear_rank3 = True

                    print("정말 대단한 일을 해내셨군요! 최종 보스들을 물리치고 에테리아 왕국을 위기에서 구해내셨습니다. ")
                    print("이제 에테리아는 다시 평화로운 삶을 되찾게 되었습니다. 이제 당신은 에테리아의 영웅이 되었습니다. ")
                    print("에테리아의 모든 주민들은 당신을 존경하며 감사하게 생각할 것 입니다.")
                    print("\n(게임에서 승리하셨습니다. 3초 후 게임이 종료됩니다.)")
                    sleep(3)
                    sys.exit()

                else:
                    is_in_dungeon = False
                    break

            # 8. 몬스터가 공격
            attack_info_list = []
            for monster in monster_list:
                if monster:
                    attack_info = monster.attack()
                    attack_info_list.append(attack_info)

            # 9. 플레이어가 피격
            for attack_info in attack_info_list:
                player.attacked(attack_info)

            # 10. 플레이어 생사 확인
            player_is_alive = player.get_status("is_alive")
            if not player_is_alive[0]:
                print("게임이 종료됩니다.")  # ✅ 반복문 탈출 수정
                is_in_dungeon = False
                game_exit = True
                break
