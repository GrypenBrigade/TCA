# Context Free Grammar

## Code snippets

**CFG Rules and Parser**

```
import nltk
from nltk import CFG, word_tokenize, TreePrettyPrinter

grammar = CFG.fromstring("""
SENTENCE -> NOUN_PHRASE VERB_PHRASE
NOUN_PHRASE -> DETERMINER NOUN | DETERMINER ADJECTIVE NOUN | DETERMINER ADJECTIVE ADJECTIVE NOUN | NOUN
VERB_PHRASE -> VERB NOUN_PHRASE | VERB NOUN_PHRASE PREPOSITIONAL_PHRASE | VERB PREPOSITIONAL_PHRASE
PREPOSITIONAL_PHRASE -> PREPOSITION NOUN_PHRASE | PREPOSITION DETERMINER NOUN

DETERMINER -> 'the' | 'a' | 'some'
NOUN -> 'Jerome' | 'dog' | 'cat' | 'telescope' | 'park' | 'car' | 'moon'
ADJECTIVE -> 'big' | 'little' | 'green' | 'quick' | 'bright' | 'dark'
VERB -> 'saw' | 'walked' | 'drove' | 'barked'  
PREPOSITION -> 'in' | 'with' | 'to' | 'at'

""")

parser = nltk.ChartParser(grammar)

```
**Sentence tokenizer and Tree generator**

```
example_sentence1 = "the big dark dog saw a quick little cat in the park"
exsent1_token = word_tokenize(example_sentence1)

print("\nExample Sentence 1 Parse Tree/s:\n")
tree1 = list(parser.parse(exsent1_token)) 
for i, tree in enumerate(tree1, 1):
    print(f"Parse Tree {i}:")
    tree.pretty_print()

```

## Sample Output
```
Example Sentence 1 Parse Tree/s:

Parse Tree 1:
                                            SENTENCE
                 ______________________________|_______________________
                |                                                 VERB_PHRASE
                |                       _______________________________|______________________________
           NOUN_PHRASE                 |              NOUN_PHRASE                              PREPOSITIONAL_PH     
                |                      |                   |                                         RASE
     ___________|_________________     |        ___________|___________________          _____________|__________    
DETERMINER  ADJECTIVE  ADJECTIVE NOUN VERB DETERMINER  ADJECTIVE   ADJECTIVE  NOUN PREPOSITION    DETERMINER    NOUN
    |           |          |      |    |       |           |           |       |        |             |          |   
   the         big        dark   dog  saw      a         quick       little   cat       in           the        park

Parse Tree 2:
                                            SENTENCE
                 ______________________________|_______________________
                |                                                 VERB_PHRASE
                |                       _______________________________|______________________________
                |                      |                   |                                   PREPOSITIONAL_PH
                |                      |                   |                                         RASE
                |                      |                   |                             _____________|______________
           NOUN_PHRASE                 |              NOUN_PHRASE                       |                       NOUN_PHRASE     
     ___________|_________________     |        ___________|___________________         |              ______________|_______    
DETERMINER  ADJECTIVE  ADJECTIVE NOUN VERB DETERMINER  ADJECTIVE   ADJECTIVE  NOUN PREPOSITION    DETERMINER                NOUN
    |           |          |      |    |       |           |           |       |        |             |                      |   
   the         big        dark   dog  saw      a         quick       little   cat       in           the                    park


```


Jerome Estomago Talaro BSCS501 TCA