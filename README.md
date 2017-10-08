# "Diceware" Password Generator. 

## Usage
    usage: get_pw.py [-h] [-w WORDS] [-p PASSWORDS] [-wf WORD_FILE]

    optional arguments:
      -h, --help            show this help message and exit
      -w WORDS, --words WORDS
                        Number of words to generate in the password. Defaults
                        to 5.
      -p PASSWORDS, --passwords PASSWORDS
                        Number of passwords to generate. Defaults to 20.
      -wf WORD_FILE, --word-file WORD_FILE
                        Dice Word File. Defaults to ./eff_large_wordlist.txt.


## Notes
    Files:
        eff_large_wordlist.txt
        get_pw.py

    Description:
        "Diceware" implementation of random passwords generator.
        In addition to generating a word from a wordlist,
        the program has a probability
        of generating a number or a symbol instead of a word.

        It also has a probability of converting a word to Title Case.
        
        Using real dice to lookup entries from the list will be 
        more random than using a pseudo-random generator, as used here. 
        This is a good tool, and probably random enough. 
        
        Not all passwords generated will be appropriate for every use-case
        or set of input limitations.  Generate a bunch of them and 
        cherry-pick the ones most appropriate. 
        
        (Or, clone and modify this script for use)

## Example
    /PATH/TO/SCRIPT/diceware_password> python3 get_pw.py
    
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
