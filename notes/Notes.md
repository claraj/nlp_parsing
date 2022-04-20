Lectures 
* March 25th, 25:30 -> End 

https://minnstate.zoom.us/rec/play/U1KeYesdVUsZvyqK6rur3jnWwOJWYuserqXPOu8KBl5_W_Mm-n-9BgN16FY_1XNuaspplGq0zOPeEOQH.RGdcriYyidoXCL11?startTime=1648234580000&_x_zm_rtaid=9nD2UGQyScKLwsaXORBDdw.1650072533771.0b7196dd9a74fdfd3f54582530a07dee&_x_zm_rhtaid=255

* March 28 

https://minnstate.zoom.us/rec/play/843UtECOSYdeN6mofGiMr4DbixBR3ePkl-d09roRAaLtEYUOl3WFnbXGReIPzqERWwArg8n1wV9WayiT.fLLPAYLXvU4K6jT0?startTime=1648494070000&_x_zm_rtaid=9nD2UGQyScKLwsaXORBDdw.1650072533771.0b7196dd9a74fdfd3f54582530a07dee&_x_zm_rhtaid=255

* March 30 And the following week
Link.....



Finite state automata 
Finite state machines 
Augmented transition networks 

S-Expression or symbolic expression 
https://en.wikipedia.org/wiki/S-expression


Building a representation of the sentence structure - what does each word represent in the sentence? What does it do in the sentence?  

Questions:
* Can we assume the sentences are ( MOOD declarative )  ? (yes)
* Will allow up to one adverb to go before or after a verb to form a verb phrase
    * adverb = word that modifies a verb ("almost" "very" "quietly", "especially")
    * VP can also be just a verb.


ATN 

Inputs are words 

Augmented = actions associated with transitions 

Parts of a parse can be sets - { present, past } if it is ambiguous.

\* is for the word or phrase that allowed us to traverse the arc.

Enter at the node marked NP
Cross an arc when the next input word matches its label, and carry out associated actions

Two assignment action associated with the PRONOUN arc:

1. Set PRONOUN to *, the word processed to traverse the arc ("we")
2. Assign the person and number of the word ("we" is 1p = first person plural)

The input word prcessed must match the arc's label (like "pronoun")

Follow the done arc to exit the network, return a list of pairs labeled by the ATN's name (like NP)

( NP ( PRONOUN we )  (NUM 1p ) )

System must examine lexicon to decide if a word will match a node in a ATN