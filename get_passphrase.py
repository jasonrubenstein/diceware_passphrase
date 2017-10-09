#! /usr/bin/python3
import argparse
import os
import time
from random import SystemRandom

sys_rand = SystemRandom(os.urandom(256))

ROLL_OF_SYMBOL = sys_rand.randrange(19,32)

ROLL_OF_NUMBER = sys_rand.randrange(5, 35)
ROLL_OF_TITLECASE = sys_rand.randrange(35,62)
GENERAL_CASE = 100
LENGTH_OF_WORDLIST_KEY = 5

VALID_CASES_WORD_CHAOS = (
  ROLL_OF_NUMBER,
  ROLL_OF_TITLECASE,
  GENERAL_CASE,
)

WORD_FILE = "./eff_large_wordlist.txt"
WORD_DICT = {}

NO_DICE_WORD_FILE = "./diceware8k.txt"
NO_DICE_WORD_LIST = []

nums = tuple(map(str, (0,1,2,3,4,5,6,7,8,9)))
syms = ('&', '.', '-', '$', '_', '@', '!')

mapper = {
  ROLL_OF_NUMBER: lambda x: ''.join(sys_rand.sample(nums, sys_rand.randint(2,7))),
  ROLL_OF_TITLECASE: lambda x: x.title(),
  GENERAL_CASE: lambda x: x
}

WORDS_TO_GENERATE = 7
PASSPHRASES_TO_GENERATE = 20

map_target_list = []
for i in range(100):
    for k in VALID_CASES_WORD_CHAOS:
        if i <= k:
            map_target_list.append(k)
            break
            map_target_list.append(GENERAL_CASE)


def _roll_d100():
    coinflip = sys_rand.choice((0,1))
    return sys_rand.gauss(0.5, 0.5).as_integer_ratio()[coinflip] % 100


def _insert_symbol(passphrase):
    sym = sys_rand.choice(syms)
    indices = [i for i,char in enumerate(passphrase) if char.isspace()]
    idx = sys_rand.choice(indices)
    new_passphrase = "{}{}{}".format(passphrase[:idx], sym, passphrase[idx+1:])
    return new_passphrase


def _create_word_dict(word_file):
    global WORD_DICT
    fd = open(word_file, 'r')
    raw = fd.read()
    words = raw.split('\n')
    WORD_DICT = {x[0]:x[1] for x in [e.split("\t") for e in words] if len(x) == 2}


def _create_no_dice_word_list(word_file):
    global NO_DICE_WORD_LIST
    fd = open(word_file, 'r')
    raw = fd.read()
    words = raw.split('\n')
    NO_DICE_WORD_LIST = [w for w in words if w]


def _probable_chaos(werd):
    d100 = _roll_d100()
    probability_case = map_target_list[d100]
    werd = mapper.get(probability_case, lambda x: None)(werd)
    return werd


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
    werd = _probable_chaos(werd)

    return werd


def get_word_no_dice():
    '''
        Gets a word from the 8k word list, and rolls d100 to
        find the probability of a mutation.
    '''
    werd = sys_rand.choice(NO_DICE_WORD_LIST)
    werd = _probable_chaos(werd)

    return werd


def get_pw(num_words, no_dice):
    if not WORD_DICT:
        _create_word_dict(WORD_FILE)

    word_getter = get_word
    if no_dice:
        word_getter = get_word_no_dice
        if not NO_DICE_WORD_LIST:
            _create_no_dice_word_list(NO_DICE_WORD_FILE)

    pw_list = []
    for j in range(num_words):
      pw_list.append(word_getter())
    passphrase =  ' '.join(pw_list)

    if _roll_d100() <= ROLL_OF_SYMBOL:
        passphrase = _insert_symbol(passphrase)

    return passphrase

if __name__ == "__main__":
    description = '''
        Files:
          eff_large_wordlist.txt
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
    parser.add_argument(
        "-wf",
        "--word-file",
        type=str,
        default=WORD_FILE,
        help="Dice Word File. Defaults to {}.".format(WORD_FILE),
      )
    parser.add_argument(
      "-nd",
      "--no_dice",
      default=False,
      action='store_true',
      help='''true | false. Executes a 'no dice' version.
Executes a uniform distribution random get from a list of 2**13 words.''',
    )
    args = parser.parse_args()

    _create_word_dict(args.word_file)

    divvy = ''.join(['*' for x in range(80)])
    print(' ')
    print(divvy)
    for j in range(args.passphrases):
      pw = get_pw(args.words, args.no_dice)
      print(pw)
    print(divvy)
    print(' ')
