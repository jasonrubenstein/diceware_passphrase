#! /usr/bin/python3
import argparse
import os
import time
from random import SystemRandom

sys_rand = SystemRandom(os.urandom(256))

ROLL_OF_SYMBOL = sys_rand.randrange(5,15)
ROLL_OF_NUMBER = sys_rand.randrange(15, 35)
ROLL_OF_TITLECASE = sys_rand.randrange(35,62)
GENERAL_CASE = 100
LENGTH_OF_WORDLIST_KEY = 5

VALID_CASES = (
  ROLL_OF_SYMBOL,
  ROLL_OF_NUMBER,
  ROLL_OF_TITLECASE,
  GENERAL_CASE,
)

WORD_FILE = "./diceware8k.txt"
WORD_LIST = []

nums = tuple(map(str, (0,1,2,3,4,5,6,7,8,9)))
syms = ('&', '.', '-', '$', '_')

mapper = {
  ROLL_OF_SYMBOL: lambda x: sys_rand.choice(syms),
  ROLL_OF_NUMBER: lambda x: ''.join(sys_rand.sample(nums, sys_rand.randint(2,7))),
  ROLL_OF_TITLECASE: lambda x: x.title(),
  GENERAL_CASE: lambda x: x
}

WORDS_TO_GENERATE = 7
PASSPHRASES_TO_GENERATE = 20

map_target_list = []
for i in range(100):
    for k in VALID_CASES:
        if i <= k:
            map_target_list.append(k)
            break
            map_target_list.append(GENERAL_CASE)


def _create_word_list(word_file):
    global WORD_LIST
    fd = open(word_file, 'r')
    raw = fd.read()
    words = raw.split('\n')
    WORD_LIST = [w for w in words if w]


def get_word():
    '''
        Gets a word from the 8k word list, and rolls d100 to
        find the probability of a mutation.
    '''
    werd = sys_rand.choice(WORD_LIST)

    coinflip = sys_rand.choice((0,1))
    d100 = sys_rand.gauss(0.5, 0.5).as_integer_ratio()[coinflip] % 100
    probability_case = map_target_list[d100]
    werd = mapper.get(probability_case, lambda x: None)(werd)

    return werd


def get_pw(num_words):
    if not WORD_LIST:
        _create_word_list(WORD_FILE)

    pw_list = []
    for j in range(num_words):
      pw_list.append(get_word())

    return ' '.join(pw_list)


if __name__ == "__main__":
    description = '''
        Files:
          diceware8k.txt
          get_passphrase.py

        Description:
         "Diceware" implementation of random passphrases generator.
         In addition to generating a word from a wordlist,
         the program has a probability
         of generating a number or a symbol instead of a word.

         It also has a probability of converting a word to Title Case.
    '''
    parser = argparse.ArgumentParser(epilog = description)
    parser.add_argument(
      "-w",
      "--words",
      type=int,
      default=WORDS_TO_GENERATE,
      help="Number of words to generate in the passphrase. Defaults to {}.".format(WORDS_TO_GENERATE),
    )
    parser.add_argument(
        "-p",
        "--passphrases",
        type=int,
        default=PASSPHRASES_TO_GENERATE,
        help="Number of passphrases to generate. Defaults to {}.".format(PASSPHRASES_TO_GENERATE),
      )
    args = parser.parse_args()

    _create_word_list(WORD_FILE)

    divvy = ''.join(['*' for x in range(80)])
    print(' ')
    print(divvy)
    for j in range(args.passphrases):
      pw = get_pw(args.words)
      print(pw)
    print(divvy)
    print(' ')
