lexicon = {
    'what': { 
        'type': 'wh-pronoun',
        'features': [ 
            {
                'feature': 'NUM',
                'values': ['3s', '3p']
            }
        ] 
    },

   'Mary': { 
        'type': 'name',
    },

    # todo "did" - is lexicon correct? 

    'did': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': ['do']
            },
            {
                'feature': 'TYPE',
                'values': ['transitive', 'bitransitive']
            },
            {
                'feature': 'TENSE',
                'values': ['past']
            },
            {
                'feature': 'NUM',
                'values': ['1s', '1p', '2s', '2p', '3s', '3p']
            },
        ] 
    },
    
    'walks': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': ['walk']
            },
            {
                'feature': 'TENSE',
                'values': ['present']
            },
            {
                'feature': 'NUM',
                'values': ['3s']
            },
        ] 
    },

    'walked': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': ['walk']
            },
            {
                'feature': 'TENSE',
                'values': ['past']
            },
            {
                'feature': 'NUM',
                'values': ['1s', '1p', '2s', '2p', '3s', '3p']
            },
        ] 
    },

    'give': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': ['give']
            },
            {
                'feature': 'TYPE',
                'values': ['transitive', 'bitransitive']
            },
            {
                'feature': 'TENSE',
                'values': ['infinitive', 'present']
            },
            {
                'feature': 'NUM',
                'values': ['1s', '1p', '2s', '2p', '3p']
            },
        ] 
    },

    'gave': { 
        'type': 'verb',
        'features': [ 
            {
                'feature': 'VERB',
                'values': ['give']
            },
            {
                'feature': 'TYPE',
                'values': ['transitive', 'bitransitive']
            },
            {
                'feature': 'TENSE',
                'values': ['past']
            },
            {
                'feature': 'NUM',
                'values': ['1s', '1p', '2s', '3s', '3p']
            },
        ] 
    },

    'me': { 
        'type': 'pronoun',
        'features': [ 
            {
                'feature': 'NUM',
                'values': ['1s']
            }
        ] 
    },

    'a': { 
        'type': 'article',
        'features': [ 
            {
                'feature': 'NUM',
                'values': ['3s']
            }
        ] 
    },

    'the': { 
        'type': 'article',
        'features': [ 
            {
                'feature': 'NUM',
                'values': ['3s', '3p']
            }
        ] 
    },

    'her': { 
        'type': 'article',
        'features': [ 
            {
                'feature': 'ROOT',
                'values': ['she']
            },
            {
                'feature': 'NUM',
                'values': ['3s', '3p']
            },
        ] 
    },

    'picture': { 
        'type': 'noun',
        'features': [ 
            {
                'feature': 'NOUN',
                'values': ['picture']
            },
            {
                'feature': 'NUM',
                'values': ['3s']
            },
        ] 
    },

    'man': { 
        'type': 'noun',
        'features': [ 
            {
                'feature': 'NOUN',
                'values': ['man']
            },
            {
                'feature': 'NUM',
                'values': ['3s',]
            },
        ] 
    },
    
    'dreams': { 
        'type': 'noun',
        'features': [ 
            {
                'feature': 'NOUN',
                'values': ['dream']
            },
            {
                'feature': 'NUM',
                'values': ['3p',]
            },
        ] 
    },

    'boat': { 
        'type': 'noun',
        'features': [ 
            {
                'feature': 'NOUN',
                'values': ['boat']
            },
            {
                'feature': 'NUM',
                'values': ['3p',]
            },
        ] 
    },

    'of': { 
        'type': 'preposition',
        'features': [ 

        ] 
    },

    

}