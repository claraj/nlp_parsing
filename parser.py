from lexicon import lexicon



def main():
    # sentence = input('Please enter your sentence: ')
    sentence = 'Mary walks'
    parse(sentence)


def parse(sentence):
    # todo lol
    words = sentence.split() 

    first_word = words[0]

    out = [ 'S', ]

    # handle arcs, and actions 


if __name__ == '__main__':
    main()