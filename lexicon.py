lexicon = {
    'what': { 
        'type': 'wh-pronoun',
        'features': [ 
            {
                'feature': 'NUM',
                'values': {'3s', '3p'}
            }
        ] 
    },

   'Mary': { 
        'type': 'name',
    },


    'purple': {
        'type': 'adj'
    },

#     # todo "did" - is lexicon correct? 
#  probably won't use here...?

    'did': { 
        'type': 'verb',
        'features': {
            'VERB': {'do'},
            'TYPE': {'transitive', 'bitransitive'},
            'TENSE': {'past'},
            'NUM': {'1s', '1p', '2s', '2p', '3s', '3p'} 
        },
    },
    
    'walks': { 
        'type': 'verb',
        'features': {
            'VERB': {'walk'},
            'TENSE': {'present'},
            'NUM': {'3s'}
        }
    },

    'walked': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': {'walk'}
            },
            {
                'feature': 'TENSE',
                'values': {'past'}
            },
            {
                'feature': 'NUM',
                'values': {'1s', '1p', '2s', '2p', '3s', '3p'}
            },
        ] 
    },

    'give': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': {'give'}
            },
            {
                'feature': 'TYPE',
                'values': {'transitive', 'bitransitive'}
            },
            {
                'feature': 'TENSE',
                'values': {'infinitive', 'present'}
            },
            {
                'feature': 'NUM',
                'values': {'1s', '1p', '2s', '2p', '3p'}
            },
        ] 
    },

    'gave': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': {'give'}
            },
            {
                'feature': 'TYPE',
                'values': {'transitive', 'bitransitive'}
            },
            {
                'feature': 'TENSE',
                'values': {'past'}
            },
            {
                'feature': 'NUM',
                'values': {'1s', '1p', '2s', '3s', '3p'}
            },
        ] 
    },

    'me': { 
        'type': 'pronoun',
        'features': [ 
            {
                'feature': 'NUM',
                'values': {'1s'}
            }
        ] 
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
        'type': 'article',
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