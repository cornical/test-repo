import sys
import string
import timeit

# Given a stream of text on stdin, report on stdout the number 
# of times each word appears, sorted by mentions with the most 
# often mentioned word first. To break a tie, order the words 
# in lexicographical order.

def count_words(lines):
    reg = {}
    for line in lines:
        for word in get_words(line):
            reg[word] = reg.get(word, 0) + 1
    return sorted(reg.items(), key=lambda tuple: (-tuple[1], tuple[0]))

def get_words(line):
    return line.lower().translate(None, string.punctuation).split()

if __name__ == '__main__':
    start_time = timeit.default_timer()
    stream = sys.stdin
    lines = sys.stdin.readlines()
    for word, count in count_words(lines):
        print word, count
    print str(timeit.default_timer() - start_time)