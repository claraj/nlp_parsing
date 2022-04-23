
from sre_parse import expand_template
from lexicon import lexicon

"""

NP - verb    <- we read ; the dog ; Zoe
np - verb - np  <- we read to the dog ; the dog ate flour ; Zoe gave a boat
np - verb - np - np <- we read a book to the dog ; the dog ate a bag of flour ; Zoe gave Mary a purple boat 



"""

from pprint import pprint

example_sentences = [
    'boat',  # ok
    'pictures',  #ok
    'a picture',
    'a small purple picture',   # noun phrase with adjectives
    'Mary sailed',  # NP, V
    'Mary gave me a picture',  # NP V NP NP
    'Mary gave Zoe a purple picture',  # NP V NP NP
    'Mary gave the large green boat a small purple picture',  # NP V NP NP   
    'a large purple man sailed the small green boat',  
    'a large purple man sailed the small green boat to Mary',  # Prepositional phrase
    'Alice gave Bob a picture of the boat',    

    # this correctly fails because the the number of verb and subject do not match
    # 'Alice give Bob a picture of the boat',    
]



def main():
    sentence = input('Please enter a sentence:\n')
    parse_sentence(sentence)


def parse_sentence(sentence):
    # convert to lowercase, except names, which are assumed to start with a capital 
    sentence = sentence.lower()
    words = sentence.split()
    for index, word in enumerate(words):
        if word in lexicon:
            continue
        if word.capitalize() in lexicon:
            words[index] = word.capitalize()  # re-capitalize names 

    parse = ATN(words)
    pprint(parse)


def ATN(words):

    for word in words:
        if not lexicon.get(word):
            raise Exception(f'Word {word} not in lexicon.')

    noun_parse, position, NUM_NP = NP_1(words, 0)

    parse = [ ('MOOD', 'declarative'), ('SUBJ', noun_parse), ]

    if position >= len(words):
        sentence = ( 'S', tuple(parse) )
        return sentence

    verb_parse = V(words, position, NUM_NP)

    parse.append(verb_parse)

    sentence = ( 'S', tuple(parse) )
    return sentence


def V(words, position, NUM_NP):

    verb_parse = [ 'V', ] 

    verb = words[position]  # assuming one verb 

    # ensure passes test NUM(SUBJ) ⋂ NUM(*)
    verb_lexicon_entry = lexicon[verb]
    num_verb = verb_lexicon_entry['features']['NUM']
    num_intersect = sets_intersect(NUM_NP, num_verb)
    tense = verb_lexicon_entry['features']['TENSE']

    if num_intersect:  # non-empty set
        part_verb_parse = ( ('VERB', verb), ('NUM', num_intersect ), ('TENSE', tense) ) 
    else:
        raise Exception(f'Verb does not make sense. {verb} {verb_lexicon_entry} \n{words}')

    verb_parse.append(part_verb_parse)

    position += 1

    if position >= len(words):
        return tuple(verb_parse)

    # do we do NP stuff to S3 or jump to S3? 
    # test - is this verb transitive or not? 
    verb_type = verb_lexicon_entry['features']['TYPE']  # eg. transitive, bitransitive

    if 'transitive' in verb_type:
        # go to S2 via NP 
        object_noun_parse, position, NUM = NP_1(words, position)

        object_stuff = (  ('OBJ', object_noun_parse) )   
        verb_parse.append(object_stuff)
        
    else:
        # jump to S3
        pass 

    if position >= len(words):
        return tuple(verb_parse)



    # from s3, where now? jump or via NP?
    if 'bitransitive' in verb_type:
        # IND-OBJ = OBJ
        # OBJ = *
        indirect_object_noun_parse, position, NUM = NP_1(words, position)
        
        verb_parse.pop()  # remove the object? 
        object_stuff_again = ( ( 'OBJ', object_noun_parse) , ('IND-OBJ', indirect_object_noun_parse) ) 
        verb_parse.append(object_stuff_again)   # don't want to re-add the object? 

    else:
        # jump, done 
        pass 

    return tuple(verb_parse)
    

def PP(words, position):

    preposition = words[position]

    prep_parse = [  ] 

    lexicon_entry = lexicon[preposition]

    match lexicon_entry['type']:
        case 'pp-noun':
            prep_parse.append( ('PP', preposition) )
            # and done 
        case 'preposition':
            prep_parse.append( ('PREP', preposition) )
            # now deal with NP 
            np_parse = NP_1(words, position=position + 1)
            prep_parse.append( ('OBJ', np_parse) )

    prep_parse_with_modifiers = ('MODS', prep_parse)
    return tuple(prep_parse_with_modifiers)


# the big noun phrase ATN. Deals with "we read", "the cat", "the big blue cat", "Zoe" etc. 
def NP_1(words, position=0):

    # return the list container AND the NUM and the noun and the position we are at 

        out = [ 'NP', ]

    # for index in range(position, len(words)):
    # for index, word in enumerate(words):   # not sure the loop is necessary here

        word = words[position]

        lexicon_entry = lexicon[word]
        features = lexicon_entry.get('features')
        if features:
            NUM = features.get('NUM')
            if len(NUM) == 1:
                NUM = list(NUM)[0]  # if a set of 1 thing, convert to string for cleaner output 
        else:
            NUM = set()

        match lexicon_entry['type']:
            case 'article':
                article = ( ('DET', word), ('NUM', NUM))
                # todo article -> adjective loop 
                out.append(article)
                from_np_2, position = NP_2(words, NUM, position + 1, adj=[])
                out.append(from_np_2)
            case 'pronoun':
                pronoun = ( ('PRONOUN', word), ('NUM', NUM ) )
                out.append(pronoun)
            case 'noun':
                if NUM == '3s' or '3s':
                    noun = ( ('NOUN', word), ('NUM', NUM ) )
                    out.append(noun)
                # elif NUM == '3p':
                #     noun = ( ('NOUN', word), ('NUM', '3p' ) )
                #     out.append(noun)
                else:
                    raise Exception(f'Noun does not make sense. "{word}" with lexicon entry {lexicon_entry}. Current words: {words}')
            case 'name':
                name = ( ('NAME', word), ('NUM', '3s') )
                out.append(name)
            case 'preposition':
                prep_parse = PP(words, position)  
                out.append(prep_parse)              

            case _:   # the default case, nothing else matches
                raise Exception(f'Unexpected word type "{word}" with lexicon entry {lexicon_entry}.  Current words: {words}')

        return tuple(out), position + 1, NUM


# Handles adjectives, "big" and "purple" in "the big purple cat"
# outputs something like ( (NOUN, cat) ( ADJS, { big, purple } ) )
def NP_2(words, NUM, position, adj = []):

    word = words[position]

    lexicon_entry = lexicon[word]

    match lexicon_entry['type']:
        case 'adj':
            adj.append(word)
            return tuple(NP_2(words, NUM, position + 1, adj))
            
        case 'noun':
            # NUM(*)  must be in the set NUM
            num_intersect = sets_intersect(lexicon_entry['features']['NUM'], NUM)
            if num_intersect:
                if adj:
                    parse = ( ('NOUN', word ),  ('NUM', num_intersect ),  ( 'ADJ', adj) )
                else:
                    parse = ( ('NOUN', word ),  ('NUM', num_intersect ) )
                return parse, position
            else:
                raise Exception(f'Noun should match number {NUM}. {word} {lexicon_entry} \n{words}')

        case _:
            raise Exception(f'Unexpected type. {word} {lexicon_entry} \n{words}')


def sets_intersect(num_1, num_2):

    # either a string, or a set of strings. 
    if isinstance(num_1, str):
        num_1 = { num_1, }
    if isinstance(num_2, str):
        num_2 = { num_2, }
        
    return num_1.intersection(num_2)



for example in example_sentences:
    print(example)
    try:
        parse_sentence(example)
    except Exception as e:
        print('Cannot parse sentence because', e)