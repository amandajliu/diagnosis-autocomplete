from Trie import Trie

t = Trie()
words = []
with open('short-diagnoses.txt', 'r') as f:
    for line in f:
        full_word = line.strip()
        if full_word.find("(") != -1 and full_word.find(")") != -1:
            alternate_name = full_word[full_word.find("(")+1:full_word.find(")")]
            t.addWord(alternate_name, line.strip())
        t.addWord(line.strip())
t.addWord('hello')
t.addWord('hellobanana')
t.addWord('bl')
t.addWord('bla k')
t.addWord('bla bla ()')
print("middle", t.autocomplete('middle'))
print("shorts", t.autocomplete("shorts"))
print("hi", t.autocomplete('he'))
print("bl ", t.autocomplete('bl '))
print("bla", t.autocomplete('bla'))
print("he", t.autocomplete('he'))
print("ar", t.autocomplete("ar"))
print(t.words)
