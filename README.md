# "Diceware" passphrase Generator.

## Usage
    usage: get_passphrase.py [-h] [-w WORDS] [-p PASSPHRASES] [-wf WORD_FILE]
                             [-nd]

    optional arguments:
      -h, --help            show this help message and exit
      -w WORDS, --words WORDS
                            Number of words to generate in the passphrase.
                            Defaults to 7.
      -p PASSPHRASES, --passphrases PASSPHRASES
                            Number of passphrases to generate. Defaults to 20.
      -wf WORD_FILE, --word-file WORD_FILE
                            Dice Word File. Defaults to ./eff_large_wordlist.txt.
      -nd, --no_dice        Executes a 'no dice' version; a
                            uniform distribution random selection from a list
                            of 2**13 words.



## Notes
    Files:
        eff_large_wordlist.txt
        diceware8k.txt
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
    /PATH/TO/SCRIPT/diceware_passphrase> python3 get_passphrase.py

    ********************************************************************************
    job profane 87963 crawling 0789 disparate covenant
    & 8563 dragonfly dullness showpiece oaf 73509
    . 81237 263719 omega decay 5367 diabetes
    payer 85906 12 decent armchair celestial -
    & 72 humorless crabmeat croon catty 206
    datebook basin elk astound 2490781 7106985 moonlit
    reopen boil dealt rind 89 63 anthem
    cesarean richness . graceful chivalry Demanding 348
    drier alibi smoking 73058 chasing 08459 765
    second Reusable designed oil 1270 dab rocklike
    astonish boxy 7016239 basil opt 7139240 02437
    atlas gloater 1508792 broiler applicant joyride chowder
    _ 872 ashen & 1867523 asparagus obscurity
    $ 6095814 dupe cornball nest gummy showoff
    _ 97 8546 probe sacrifice creamlike countless
    deacon kung dejected dumpling phonics disdain 03
    chitchat ashamed hug kiwi armchair drinkable disfigure
    disclose corrode repayment oil flakily rubble dicing
    251 smilingly Dating cyclic 63851 groom oops
    hypertext 86 matador crewless jigsaw 1092435 drainage
    ********************************************************************************

    
    /PATH_TO_SCRIPT/diceware_passphrase> ./get_passphrase.py -nd  
 
    ********************************************************************************
    slip Abide 0427 shinto chord mess Lope
    pawn Si Equal gain shot Gleam Odin
    livid Lh 940875 zm wok vicar Apart
    clap Mace Grata 34215 wing Ho brow
    wino loon frye shave mugho 5g She
    weigh climb 847 core j3 vellum Gourd
    phyla beggar - Alamo muong suny It
    Guam faery Datum Among w's Eaten Riley
    hire beth 508124 child Papal 2548 Wynn
    alien shed Crony 2000 Wild extent Egan
    washy Proxy see Yq 6Th Petri -
    lykes l6 3684759 nat where 26 186
    bongo & Lp ru sorry spate sharp
    signor Carry bowel sand Duffy Rest 184936
    sawyer Mila slid snarl pusan we'd Loll
    Mot Dddd Samoa Alton 6Q Scamp Until
    Wahl livid Yeasty Hoof Tavern t3 Radium
    902145 If Crab lamar 032 efg Kx
    plank totem Tulsa honda bh len clan
    333 ohio Kp molar Gp fudge nt
    ********************************************************************************

