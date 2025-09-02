import nltk

from nltk import CFG, word_tokenize, TreePrettyPrinter

# grammar rules and parser

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


# sentences and tokenization
example_sentence1 = "the big dark dog saw a quick little cat in the park"
example_sentence2 = "Jerome saw the bright moon with a telescope"
example_sentence3 = "some big dog barked at Jerome"
example_sentence4 = "Jerome drove a big green car to the park"

exsent1_token = word_tokenize(example_sentence1)
exsent2_token = word_tokenize(example_sentence2)
exsent3_token = word_tokenize(example_sentence3)
exsent4_token = word_tokenize(example_sentence4)

# tree generation
print("Sentences that have more than 1 parse tree means the sentence is structured ambiguously.\n")

print("\nExample Sentence 1 Parse Tree/s:\n")
tree1 = list(parser.parse(exsent1_token)) 
for i, tree in enumerate(tree1, 1):
    print(f"Parse Tree {i}:")
    tree.pretty_print()

print("\nExample Sentence 2 Parse Tree/s:\n")
tree2 = list(parser.parse(exsent2_token))
for e, tree in enumerate(tree2, 1):
    print(f"Parse Tree {e}:")
    tree.pretty_print()

print("\nExample Sentence 3 Parse Tree/s:\n")
tree3 = list(parser.parse(exsent3_token))
for a, tree in enumerate(tree3, 1):
    print(f"Parse Tree {a}:")
    tree.pretty_print()

print("\nExample Sentence 4 Parse Tree/s:\n")
tree4 = list(parser.parse(exsent4_token))
for b, tree in enumerate(tree4, 1):
    print(f"Parse Tree {b}:")
    tree.pretty_print()


