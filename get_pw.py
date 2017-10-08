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
LENGTH_OF_WORDLIST_KEY = 7

VALID_CASES = (
  ROLL_OF_SYMBOL,
  ROLL_OF_NUMBER,
  ROLL_OF_TITLECASE,
  GENERAL_CASE,
)

WORD_FILE = "./eff_large_wordlist.txt"
WORD_DICT = {}

nums = tuple(map(str, (0,1,2,3,4,5,6,7,8,9)))
syms = ('&', '.', '-', '$', '_')

mapper = {
  ROLL_OF_SYMBOL: lambda x: sys_rand.choice(syms),
  ROLL_OF_NUMBER: lambda x: ''.join(sys_rand.sample(nums, sys_rand.randint(2,7))),
  ROLL_OF_TITLECASE: lambda x: x.title(),
  GENERAL_CASE: lambda x: x
}

WORDS_TO_GENERATE = 6
PASSWORDS_TO_GENERATE = 20

map_target_list = []
for i in range(100):
    for k in VALID_CASES:
        if i <= k:
            map_target_list.append(k)
            break
            map_target_list.append(GENERAL_CASE)


def _create_word_dict(word_file):
    global WORD_DICT
    fd = open(word_file, 'r')
    raw = fd.read()
    words = raw.split('\n')
    WORD_DICT = {x[0]:x[1] for x in [e.split("\t") for e in words] if len(x) == 2}


def get_word():
    '''
        Gets a word from the dice-word-list (via 5xd6), and rolls d100 to
        find the probability of a mutation.
    '''
    diceroll = []

    for i in range(LENGTH_OF_WORDLIST_KEY):
        coinflip = sys_rand.choice((0,1))
        val = sys_rand.random().as_integer_ratio()[coinflip] % 6
        diceroll.append(str(val))

    key = ''.join(diceroll)
    werd = WORD_DICT[key]

    coinflip = sys_rand.choice((0,1))
    d100 = sys_rand.gauss(0.5, 0.5).as_integer_ratio()[coinflip] % 100
    probability_case = map_target_list[d100]
    werd = mapper.get(probability_case, lambda x: None)(werd)

    return werd


def get_pw(num_words):
    if not WORD_DICT:
        _create_word_dict(WORD_FILE)

    pw_list = []
    for j in range(num_words):
      pw_list.append(get_word())

    return ' '.join(pw_list)


if __name__ == "__main__":
    description = '''
        Files:
          eff_large_wordlist.txt
          get_pw.py

        Description:
         "Diceware" implementation of random passwords generator.
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
      help="Number of words to generate in the password. Defaults to {}.".format(WORDS_TO_GENERATE),
    )
    parser.add_argument(
        "-p",
        "--passwords",
        type=int,
        default=PASSWORDS_TO_GENERATE,
        help="Number of passwords to generate. Defaults to {}.".format(PASSWORDS_TO_GENERATE),
      )
    parser.add_argument(
                "-wf",
                "--word-file",
                type=str,
                default=WORD_FILE,
                help="Dice Word File. Defaults to {}.".format(WORD_FILE),
              )
    args = parser.parse_args()

    _create_word_dict(args.word_file)

    divvy = ''.join(['*' for x in range(80)])
    print(' ')
    print(divvy)
    for j in range(args.passwords):
      pw = get_pw(args.words)
      print(pw)
    print(divvy)
    print(' ')
