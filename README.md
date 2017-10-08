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
