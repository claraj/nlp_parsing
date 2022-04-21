from turtle import pos
from lexicon import lexicon

""" arc NP/Name 

Action - set NAME = * 
NUM = 3s



Operaing on the Noun Prase NP "we" 
Pronouns are a sort of noun phrase. 
"we read" "we" takes the place of a noun s "we" takes the place of  
the thing, so "Me and Tilley read"




Arc              Actions 
NP / pronoun     PRONOUN = *
                 NUM = 1p 
"""


## Noun phrase 

"""

NP - verb    <- we read ; the dog
np - verb - np  <- we read to the dog ; the dog ate flour
np - verb - np  <- we read a book to the dog ; the dog ate a bag of flour

"""

import pprint


def sets_intersect(num_1, num_2):
    # either a string, or a set of strings. 
    if isinstance(num_1, str):
        num_1 = set(num_1)
    if isinstance(num_2, str):
        num_2 = set(num_2)
    return num_1.intersection(num_2)


def ATN(words):

    for word in words:
        if not lexicon.get(word):
            raise Exception('Word {word} not in lexicon.')

    noun_parse, position = NP_1(words, 0)

    parse = [ ('MOOD', 'declarative'), ('SUBJ', noun_parse),  ]

    if position >= len(words):
        return parse

    verb = words[position]  # assuming one verb 

    # ensure passes test NUM(SUBJ) ⋂ NUM(*)
    verb_lexicon_entry = lexicon[verb]
    num_verb = verb_lexicon_entry['features']['NUM']
    num_intersect = sets_intersect(NUM_NP, num_verb)

    if num_intersect:  # non-empty set
        verb_parse = ( ('VERB', verb), ('NUM', num_intersect ) ) 
    else:
        raise Exception(f'Verb does not make sense. {verb} {verb_lexicon_entry} \n{words}')

    parse.append(verb_parse)

    position += 1

    # do we do NP stuff to S3 or jump to S3? 
    # test is - is this verb transitive or not? 

    verb_type = verb_lexicon_entry['features']['TYPE']  # eg. transitive, bitransitive

    if 'transitive' in verb_type:
        # go to S2 via NP 
        object_noun_parse, position = NP_1(words, position)

        object_stuff = (  ('OBJ', object_noun_parse) )    # glob this in somewhere 
        parse.append(object_stuff)
        
    else:
        # jump to S3
        pass 

    # from s3, where now? jump or via NP?
    if 'bitransitive' in verb_type:
        # IND-OBJ = OBJ
        # OBJ = *
        indirect_object_noun_parse, position = NP_1(words, position)
        # what about the ind-obj?
        object_stuff_again = ( ('IND-OBJ', indirect_object_noun_parse) , ( 'OBJ', object_noun_parse) ) 
        parse.append(object_stuff_again)   # don't want to re-add the object? 

    else:
        # jump, done 
        pass 

    return parse


# the big noun phrase ATN. Deals with "we read", "the cat", "the big blue cat", "Zoe" etc. 
def NP_1(words, position=0):

    # return the listy container AND the NUM and the noun and the position we are at 

    out = [ 'NP', ]

    for index, word in enumerate(words):

        lexicon_entry = lexicon[word]
        features = lexicon_entry.get('features')
        if features:
            NUM = features.get('NUM')

        match lexicon_entry['type']:
            # case 'adj':
            #     from_np_2, position = NP_2(words, word, NUM)
            #     out.append(from_np_2)
            #     return out, index + position + 1
            case 'article':
                article = [ ('DET', word), ('NUM', lexicon_entry['features']['NUM'])]
                # todo article -> adjective loop 
                out.append(article)
                from_np_2, position = NP_2(words, NUM, position + 1)
                out.append(from_np_2)
                return out, index + position + 1
            case 'pronoun':
                pronoun = [ ('PRONOUN', word), ('NUM', lexicon_entry['features']['NUM'] ) ]
                out.append(pronoun)
                return out, index + position + 1
            case 'noun':
                # TEST NUM(*) = 3p
                if NUM == {'3s'}:
                    noun = [ ('NOUN', word), ('NUM', '3s' ) ]
                    out.append(noun)
                    return out,  index + position + 1
                elif NUM == {'3p'}:
                    noun = [ ('NOUN', word), ('NUM', '3p' ) ]
                    out.append(noun)
                    return out,  index + position + 1
                else:
                    raise Exception(f'Noun does not make sense. {word} {lexicon_entry} \n{words}')
            case 'name':
                name = [ ('NAME', word), ('NUM', '3s') ]
                out.append(name)
                return out, index + position + 1
            case _:   # the default case, nothing else matches
                raise Exception(f'Unexpected word type {word} {lexicon_entry} \n{words}')


# Handles adjectives, "big" and "purple" in "the big purple cat"
# outputs something like ( (NOUN, cat) ( ADJS, { big, purple } ) )
def NP_2(words, NUM, position, adj = []):

    word = words[position]

    lexicon_entry = lexicon[word]

    match lexicon_entry['type']:
        case 'adj':
            adj.append(word)
            # return adj, position + 1, NP_2(words, NUM, position + 1, adj)
            return NP_2(words, NUM, position + 1, adj)
            
        case 'noun':
            # NUM(*)  must be in the set NUM
            num_intersect = sets_intersect(lexicon_entry['features']['NUM'], NUM)
            # if lexicon_entry['features']['NUM'] == NUM or lexicon_entry['features']['NUM'] in NUM:
            if num_intersect:
                parse = ( ('NOUN', word ),  ('NUM', num_intersect ),  ( 'ADJ', adj) )
                return parse, position
                # NUM = NUM(*) ⋂ NUM
                # return 
            else:
                raise Exception(f'Noun should match number {NUM}. {word} {lexicon_entry} \n{words}')

        case _:
            raise Exception(f'Unexpected type. {word} {lexicon_entry} \n{words}')



# example = 'a picture'.split()   # yup
example = 'a purple purple picture'.split()   # yup
# example = 'Mary'.split()  # ok
# example = 'boat'.split()  # ok
# example = 'pictures'.split()  #ok

# example = ''.split()
# example = ''.split()
pprint.pprint(ATN(example))

