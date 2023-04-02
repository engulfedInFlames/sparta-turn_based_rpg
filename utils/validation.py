def check_string_number_answer(answer: str, range_: int) -> str:
    _answer_list = [str(n) for n in range(1, range_+1)]
    _answer = answer
    while _answer not in _answer_list:
        _answer = input("입력이 잘못됐습니다. 다시 입력하세요 : ")
    return _answer


def check_yes_or_no_answer(answer: str) -> str:
    _answer_list = ["y", "yes", "n", "no"]
    _answer = answer.lower()
    while _answer not in _answer_list:
        _answer = input("입력이 잘못됐습니다. 다시 입력하세요 : ")
    return _answer


def check_name(answer: str) -> str:
    _answer = answer.strip()
    while not _answer:
        _answer = input("입력이 잘못됐습니다. 다시 입력하세요 : ")

    return _answer
