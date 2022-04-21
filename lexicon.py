lexicon = {
    'what': { 
        'type': 'wh-pronoun',
        'features': {
                'feature': 'NUM',
                'values': {'3s', '3p'}
            }
    },

   'Mary': { 
        'type': 'name',
    },


    'purple': {
        'type': 'adj'
    },

    'green': {
        'type': 'adj'
    },
    
    'small': {
        'type': 'adj'
    },

    'large': {
        'type': 'adj'
    },



#     # todo "did" - is lexicon correct? 
#  probably won't use here...?

    'did': { 
        'type': 'verb',
        'features': {
            'VERB': {'do'},
            # bitransitive is another word for ditransitive 
            'TYPE': {'transitive', 'bitransitive'},
            'TENSE': {'past'},
            'NUM': {'1s', '1p', '2s', '2p', '3s', '3p'} 
        },
    },
    
    'walks': { 
        'type': 'verb',
        'features': {
            'VERB': {'walk'},
            # walk may be intransitive, in that it does not take an object.
            # "I walk."
            # Or it may be transitive, "I walked a marathon"
            # What are the ATN rules for intransitive verbs? 
            'TYPE': {'transitive', 'intransitive', 'bitransitive'},
            'TENSE': {'present'},
            'NUM': {'3s'}
        }
    },

    'walked': { 
        'type': 'verb',
        'features':  {
            'VERB': {'walk'},
            'TENSE': {'past'},
            'TYPE': {'transitive', 'intransitive', 'bitransitive'},
            'NUM': {'1s', '1p', '2s', '2p', '3s', '3p'}
        },
    },

    'sailed': { 
        'type': 'verb',
        'features':  {
            'VERB': {'sail'},
            'TENSE': {'past'},
            'TYPE': {'transitive', 'bitransitive'},
            'NUM': {'1s', '1p', '2s', '2p', '3s', '3p'}
        },
    },

    'give': { 
        'type': 'verb',
        'features': {
            'VERB': {'give'},
            'TYPE': {'transitive', 'bitransitive'},
            'TENSE': {'infinitive', 'present'},
            'NUM': {'1s', '1p', '2s', '2p', '3p'}
        },
    },

    'gave': { 
        'type': 'verb',
        'features': {
            'VERB': {'give'},
            'TYPE': {'transitive', 'bitransitive'},
            'TENSE': {'past'},
            'NUM': {'1s', '1p', '2s', '2p', '3p'}
        },
    },

    'me': { 
        'type': 'pronoun',
        'features': {
                'feature': 'NUM',
                'values': {'1s'}
            }
    },

    'a': { 
        'type': 'article',
        'features': {
            'NUM': {'3s'}
        }
    },

    'the': { 
        'type': 'article',
        'features': {
                 'NUM': {'3s', '3p'}
            }
        
    },

    'her': { 
        'type': 'pronoun',
        'features': 
            {
                 'ROOT': {'she'},
                 'NUM': {'3s', '3p'}
            },
    },

    'picture': { 
        'type': 'noun',
        'features': 
            {
                 'NOUN' : {'picture'},
                 'NUM':  {'3s'}
            },
        
    },

    'pictures': { 
        'type': 'noun',
        'features': 
            {
                 'NOUN' : {'picture'},
                 'NUM':  {'3p'}
            },
        
    },

    'man': { 
        'type': 'noun',
        'features': 
            {
                 'NOUN' : {'main'},
                 'NUM':  {'3s'}
            },
        
    },
    
    'dreams': { 
        'type': 'noun',
        'features': 
            {
                 'NOUN' : {'dream'},
                 'NUM':  {'3p'}
            },
        
    },

    'boat': { 
        'type': 'noun',
        'features': {
             'NOUN': {'boat'},
             'NUM': {'3s',}
            },
    },

    'of': { 
        'type': 'preposition',
        'features': {
        }
    },

    

}