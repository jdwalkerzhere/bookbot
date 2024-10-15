from collections import Counter
from sys import argv
from typing import Dict


ALPHABET: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_word_count(filepath: str) -> int:
    with open(filepath, 'r') as file:
        return len(file.read().split())


def get_character_count(filepath: str) -> Dict[str, int]:
    with open(filepath, 'r') as file:
        return Counter([char.lower() for char in file.read() if char in ALPHABET])


def print_report(filepath: str) -> str:
    num_words: int = get_word_count(filepath)
    alphabet_dictionary: Dict[str, int] = get_character_count(filepath)
    header = f'------------Begin {filepath[filepath.rfind('/'):]} Report------------'
    word_count_report = f'{num_words} Found In Document'

    report = [header, word_count_report,]

    for char, count in sorted(alphabet_dictionary.items(), key=lambda x: x[1], reverse=True):
        report.append(f'The {char} character was found {count} times')

    report.append('-------------------End Report-------------------')
    return f'\n'.join(report)



if __name__ == '__main__':
    path_to_file = argv[1]
    print(print_report(path_to_file))
