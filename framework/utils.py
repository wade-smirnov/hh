import wonderwords
from framework.handlers.cases import CasesClient


def random_word() -> str:
    return wonderwords.RandomWord().word()


def morph_word_to_prepositional_case(word: str) -> str:
    word = word.split("(", 1)[0][:-1] if "(" in word else word
    prepositional_case = CasesClient.get_prepositional_case(word=word)
    expected_prepositional_case = "в " + prepositional_case.get("П")
    return expected_prepositional_case
