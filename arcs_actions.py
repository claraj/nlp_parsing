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

NP - verb    <- we read 
np - verb - np  <- we read to the dog
np - verb - np  <- we read a book to the dog 

"""

def sets_intersect(num_1, num_2):
    # either a string, or a set of strings. 
    if isinstance(num_1, str):
        num_1 = set(num_1)
    if isinstance(num_2, 'str'):
        num_2 = set(num_2)
    return num_1.intersection(num_2)


def ATN(words):

    subject, NUM_NP, position = NP_1(words, 0)

    parse = [ ('SUBJ', subject), ('MOOD', 'declarative') ]

    verb = words[position]  # assuming one verb 
    # ensure passes test NUM(SUBJ) ⋂ NUM(*)

    verb_lexicon_entry = lexicon[verb]
    num_verb = verb_lexicon_entry['features']['NUM']

    num_intersect = sets_intersect(NUM_NP, num_verb)

    if num_intersect:  # non-empty set
        # cool 
        verb_stuff = ( ('VERB', verb), ('NUM', num_intersect ) ) 
    else:
        raise Exception(f'Verb does not make sense. {verb} {verb_lexicon_entry} \n{words}')

    parse.append(verb_stuff)

    position += 1

    # do we do NP stuff to S3 or jump to S3? 
    # test is - is this verb transitive or not? 

    verb_type = verb_lexicon_entry['features']['TYPE']  # eg. transitive, bitransitive

    if 'transitive' in verb_type:
        # go to S2 via NP 
        object, NUM_NP, position = NP_1(words, position)

        object_stuff = (  ('OBJ', object) )    # glob this in somewhere 
        
    else:
        # jump to S3
        pass 

    # from s3, where now? jump or via NP?
    if 'bitransitive' in verb_type:
        # IND-OBJ = OBJ
        # OBJ = *
        object, NUM_NP, position = NP_1(words, position)
        # what about the ind-obj?
        object_stuff_again = ( ('IND-OBJ', object) , ( 'OBJ', object) ) 

    else:
        # jump, done 
        pass 

    return parse



def NP_1(words, position=0):

    out = [ 'NP', ]

    for index, word in enumerate(words):

        lexicon_entry = lexicon[word]
        NUM = lexicon_entry['features'].get('NUM')

        match lexicon_entry['type']:
            case 'article':
                article = [ ('DET', word), ('NUM', lexicon_entry['features']['NUM'])]
                # todo article loop 
                from_np_2 = NP_2(words, word, NUM)
                out.append(from_np_2)
            case 'pronoun':
                pronoun = [ ('PRONOUN', word), ('NUM', lexicon_entry['features']['NUM'] ) ]
                out.append(pronoun)
                return out
            case 'noun':
                # TEST NUM(*) = 3p
                if NUM == {'3p'}:
                    noun = [ ('NOUN', word), ('NUM', '3p' ) ]
                    out.append(noun)
                    return out, index + 1
                else:
                    raise Exception(f'Noun does not make sense. {word} {lexicon_entry} \n{words}')
            case 'name':
                name = [ ('NAME', word), ('NUM', '3s') ]
                out.append(name)
                return out
            case _:   # the default case, nothing else matches
                raise Exception(f'Unexpected word type {word} {lexicon_entry} \n{words}')


def NP_2(words, word, NUM):
    for word in words:
        lexicon_entry = lexicon[word]
        match lexicon_entry['type']:
            case 'adj':
                from_np_2 = NP_2(words, word, NUM)
                # go around again...

            case 'noun':
                # NUM(*)  must be in the set NUM
                if lexicon_entry['features']['NUM'] == NUM or lexicon_entry['features']['NUM'] in NUM:
                    NOUN = word 
                    # NUM = NUM(*) ⋂ NUM
                    pass
                else:
                    raise Exception(f'Noun should match number {NUM}. {word} {lexicon_entry} \n{words}')



example = 'a picture'.split()
print(NP_1(example))

