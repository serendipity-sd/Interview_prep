from collections import Counter
from functools import reduce
from operator import iconcat

def getSentences(text):
    return text.lower().split('.')

def getTrigrams(sentence):
    words = sentence.split()
    return [" ".join(words[i:i+3]) for i in range(len(words)-2)]

if __name__ == '__main__':
    text = sys.stdin.read()
    trigrams = Counter(reduce(iconcat, map(getTrigrams, getSentences(text)), []))
    print(max(trigrams, key=trigrams.get))
    
    """
   
Q. Can someone please explain why we need iconcat and also what is the use of trigrams.get in last line.



text = 'I came from the moon. He went to the other room. She went to the drawing room.'

You get a list of trigrams from the reduce with iconcat (+=), the reduce expands to:

(((([]+= ['I came from'])+= ['came from the'])+= ['from the moon'])+=...)

The Counter returns basically a dict with keys=trigrams and values=counts. So the code:

max(trigrams, key=trigrams.get)

has the max() function iterate through the counter keys (trigrams) and find the max, 
the key=trigrams.get sets the value that is maximized to trigrams.get(key) which is the count value, so trigrams.get('went to the') = 2

"""
