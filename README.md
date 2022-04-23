# Natural Language Parsing 

# Example inputs, and outputs

## Boat

Singular noun phrase

```
('S',
 (('MOOD', 'declarative'), ('SUBJ', ('NP', (('NOUN', 'boat'), ('NUM', '3s'))))))
```

## Pictures

Plural noun phrase

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ', ('NP', (('NOUN', 'pictures'), ('NUM', '3p'))))))
```

## A picture

Noun phrase with article

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ',
   ('NP',
    (('DET', 'a'), ('NUM', '3s')),
    (('NOUN', 'picture'), ('NUM', {'3s'}))))))
```

## A small purple picture

Noun phrase with article and adjectives

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ',
   ('NP',
    (('DET', 'a'), ('NUM', '3s')),
    (('NOUN', 'picture'), ('NUM', {'3s'}), ('ADJ', ['small', 'purple']))))))
```

## Mary sailed

Name (noun phrase) and verb

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ', ('NP', (('NAME', 'Mary'), ('NUM', '3s')))),
  ('V', (('VERB', 'sailed'), ('NUM', {'3s'}), ('TENSE', {'past'})))))
```

## Mary gave me a picture

Name (noun phrase) and transitive verb with noun phrase object 

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ', ('NP', (('NAME', 'Mary'), ('NUM', '3s')))),
  ('V',
   (('VERB', 'gave'), ('NUM', {'3s'}), ('TENSE', {'past'})),
   (('OBJ', ('NP', (('PRONOUN', 'me'), ('NUM', '1s')))),
    ('IND-OBJ',
     ('NP',
      (('DET', 'a'), ('NUM', '3s')),
      (('NOUN', 'picture'), ('NUM', {'3s'}))))))))
```

## Mary gave Zoe a purple picture

Name (noun phrase) and transitive verb with noun phrase object, with article and adjectives 

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ', ('NP', (('NAME', 'Mary'), ('NUM', '3s')))),
  ('V',
   (('VERB', 'gave'), ('NUM', {'3s'}), ('TENSE', {'past'})),
   (('OBJ', ('NP', (('NAME', 'Zoe'), ('NUM', '3s')))),
    ('IND-OBJ',
     ('NP',
      (('DET', 'a'), ('NUM', '3s')),
      (('NOUN', 'picture'), ('NUM', {'3s'}), ('ADJ', ['purple']))))))))
```

## Mary gave the large green boat a small purple picture

Name (noun phrase) and bitransitive verb with noun phrase object and indirect noun phtase object, with article and adjectives 

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ', ('NP', (('NAME', 'Mary'), ('NUM', '3s')))),
  ('V',
   (('VERB', 'gave'), ('NUM', {'3s'}), ('TENSE', {'past'})),
   (('OBJ',
     ('NP',
      (('DET', 'the'), ('NUM', {'3s', '3p'})),
      (('NOUN', 'boat'), ('NUM', {'3s'}), ('ADJ', ['large', 'green'])))),
    ('IND-OBJ',
     ('NP',
      (('DET', 'a'), ('NUM', '3s')),
      (('NOUN', 'picture'), ('NUM', {'3s'}), ('ADJ', ['small', 'purple']))))))))
```


## A large purple man sailed the small green boat

Noun phrase and transitive verb with noun phrase object, with article and adjectives 

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ',
   ('NP',
    (('DET', 'a'), ('NUM', '3s')),
    (('NOUN', 'man'), ('NUM', {'3s'}), ('ADJ', ['large', 'purple'])))),
  ('V',
   (('VERB', 'sailed'), ('NUM', {'3s'}), ('TENSE', {'past'})),
   ('OBJ',
    ('NP',
     (('DET', 'the'), ('NUM', {'3s', '3p'})),
     (('NOUN', 'boat'), ('NUM', {'3s'}), ('ADJ', ['small', 'green'])))))))
```

## A large purple man sailed the small green boat to Mary

Noun phrase and transitive verb with noun phrase object, with article and adjectives, and prepositional phrase 


```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ',
   ('NP',
    (('DET', 'a'), ('NUM', '3s')),
    (('NOUN', 'man'), ('NUM', {'3s'}), ('ADJ', ['large', 'purple'])))),
  ('V',
   (('VERB', 'sailed'), ('NUM', {'3s'}), ('TENSE', {'past'})),
   (('OBJ',
     ('NP',
      (('DET', 'the'), ('NUM', {'3s', '3p'})),
      (('NOUN', 'boat'), ('NUM', {'3s'}), ('ADJ', ['small', 'green'])))),
    ('IND-OBJ',
     ('NP',
      ('MODS',
       [('PREP', 'to'),
        ('OBJ', (('NP', (('NAME', 'Mary'), ('NUM', '3s'))), 11, '3s'))])))))))
```

## Alice gave Bob a picture of the boat

Noun phrase and transitive verb with noun phrase object, with article and adjectives, and prepositional phrase 

```
('S',
 (('MOOD', 'declarative'),
  ('SUBJ', ('NP', (('NAME', 'Alice'), ('NUM', '3s')))),
  ('V',
   (('VERB', 'gave'), ('NUM', {'3s'}), ('TENSE', {'past'})),
   (('OBJ', ('NP', (('NAME', 'Bob'), ('NUM', '3s')))),
    ('IND-OBJ',
     ('NP',
      (('DET', 'a'), ('NUM', '3s')),
      (('NOUN', 'picture'), ('NUM', {'3s'}))))))))
```