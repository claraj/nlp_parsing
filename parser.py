from lexicon import lexicon
from pprint import pprint
import arcs_actions


def main():
    # sentence = input('Please enter your sentence: ')
    sentence = 'Mary walks'
    parsed = parse(sentence)
    display_parse(parsed)


def display_parse(parsed):
    # todo make it pretty
    pprint(parsed)


def parse(sentence):
    # todo lol
    words = sentence.split()

    first_word = words[0]

    out = [ 'S', ]

    # Check if the sentence contains only words that are in the lexicon.
    for word in words:
        # locate word in Lexicon
        if not lexicon.get(word):
            print(f'This sentence has a word {word} that is not in the lexicon')
            return 

    
    # examine word 
    # look up in lexicon
    #  - what type? does it match an arc in the network? 
    for word in words:
        lexicon_entry = lexicon.get(word)
        word_type = lexicon_entry['type']

        print(word_type)

        match word_type:
            case 'noun':
                pass 
            case 'verb':
                pass 
            case 'pronoun':
                pass 
            case 'adj':
                pass
            case 'article':
                pass 
            case 'wh-pronoun':
                pass 
            case 'name':
                pass 
            case 'preposition':
                pass 

    return out




    # handle arcs, and actions


if __name__ == '__main__':
    main()
