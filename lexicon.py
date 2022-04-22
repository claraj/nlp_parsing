lexicon = {


    'to': { 
        'type': 'preposition',
        'features': {
                # ??? TODO
            }
    },

    'what': { 
        'type': 'wh-pronoun',
        'features': {
                'NUM': {'3s', '3p'}
            }
    },

   'Mary': { 
        'type': 'name',
            'features': {
                'NUM': {'3s'}
            }
    },

   'Zoe': { 
        'type': 'name',
            'features': {
                'NUM': {'3s'}
            }
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
            'NUM': {'1s', '1p', '2s', '2p', '3p'}  # no 3s
        },
    },

    'gave': { 
        'type': 'verb',
        'features': {
            'VERB': {'give'},
            'TYPE': {'transitive', 'bitransitive'},
            'TENSE': {'past'},
            'NUM': {'1s', '1p', '2s', '2p', '3s', '3p'}
        },
    },

    'loves': {
        'type': 'verb',
        'features': {
            'VERB': {'give'},
            'TYPE': {'transitive'},    
            'TENSE': {'present'},
            'NUM': {'3s'}  
        }
    },

    'coughs': { 
        'type': 'verb',
        'features': {
            'VERB': {'cough'},
            'TYPE': {'intransitive'},
            'TENSE': {'present'},
            'NUM': {'3s'}
        },
    },


    'me': { 
        'type': 'pronoun',
        'features': {
            'NUM': {'1s'}
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
        'features': {
                 'ROOT': {'she'},
                 'NUM': {'3s', '3p'}
            },
    },

    'picture': { 
        'type': 'noun',
        'features': {
                 'NOUN' : {'picture'},
                 'NUM':  {'3s'}
            },
        
    },

    'pictures': { 
        'type': 'noun',
        'features': {
            'NOUN' : {'picture'},
            'NUM':  {'3p'}
        },
    },

    'man': { 
        'type': 'noun',
        'features': {
            'NOUN' : {'main'},
            'NUM':  {'3s'}
        },
        
    },

    'food': { 
        'type': 'noun',
        'features': {
            'NUM':  {'3s'}
        },
        
    },
    
    'dreams': { 
        'type': 'noun',
        'features': {
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

    'yesterday': { 
        'type': 'pp-noun',
        'features': {
        }
    },


    

}