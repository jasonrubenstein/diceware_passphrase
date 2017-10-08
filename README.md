# "Diceware" passphrase Generator.

## Usage
    usage: get_passphrase.py [-h] [-w WORDS] [-p PASSPHRASES] [-wf WORD_FILE]

    optional arguments:
      -h, --help        show this help message and exit
      -w WORDS, --words WORDS
                        Number of words to generate in the passphrase. Defaults
                        to 7.
      -p PASSPHRASES, --passphrases PASSPHRASES
                        Number of passphrases to generate. Defaults to 20.
      -wf WORD_FILE, --word-file WORD_FILE
                        Dice Word File. Defaults to ./eff_large_wordlist.txt.


## Notes
    Files:
        eff_large_wordlist.txt
        get_passphrase.py

    Description:
        "Diceware" implementation of random passphrases generator.
        In addition to generating a word from a wordlist,
        the program has a probability
        of generating a number or a symbol instead of a word.

        It also has a probability of converting a word to Title Case.

        Using real dice to lookup entries from the list will be
        more random than using a pseudo-random generator, as used here.
        This is a good tool, and probably random enough for many use cases.
        If this is not good enough, follow the guidance here:
        http://world.std.com/~reinhold/diceware.html

        Not all passphrases generated will be appropriate for every use-case
        or set of input limitations.  Generate a bunch of them and
        cherry-pick the ones most appropriate.

        (Or, clone and modify this script for use)

#### Nota Bene...

According to the creator of diceware:     

> Generating truly random numbers using a computer is very tricky. The so-called random number generators that come with most programming libraries are nowhere near good enough. For most users dice is by far a better way to select passphrase words.

> However if you do know what you are doing, have access to a strong method for generating random numbers (e.g. Java's secureRandom class) and really need to generate passphrases using a computer, then, to insure a uniform distribution of words, it is best to using a list of words that is a whole power of two in length. I have created such a list and it is available at: http://world.std.com/~reinhold/diceware8k.txt. There is also a version designed for the C programming language. http://world.std.com/~reinhold/diceware8k.c The C version can easily be adapted for Java and many other programming languages.ttp://world.std.com/~reinhold/diceware8k.c The C version can easily be adapted for Java and many other programming languages.

To that end, an alternate script & file are included: `get_passphrase_no_dice.py` and `diceware8k.txt`


## Example
    /PATH/TO/SCRIPT/diceware_passphrase> python3 get_pw.py

    ********************************************************************************
    nearly battalion error deflation 906285
    sloppily 013 smile elite 25017
    hertz goldfish omit & Deferral
    illicitly negative joystick 5814 immersion
    browsing aloft siding disloyal overpass
    hardcover happiest repressed cartridge procurer
    - preteen gentile 916438 682
    moisten gracious daughter fraying Directive
    decade Deepen regalia cause patrol
    motocross herbicide silicon jubilant giving
    refried second seduce - overfull
    motocross Corporate antidote gush eliminate
    spoiler roundup plaster appliance illusion
    speak multiply blush drainpipe happiest
    repair payphone neon disdain camcorder
    neatness playback 2076 backward reformer
    cherisher Aflutter 21 drinkable dweeb
    _ define moving arguable dutiful
    catfish 165238 penknife 7021 crouch
    decompose rice 936072 grafting sauna
    ********************************************************************************
