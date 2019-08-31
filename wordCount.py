import re
import sys
import collections


def list_of_word(text: str):
    """ Function will get words of a string and put them on a list"""
    regular_expression = re.findall(r'\w+', text)

    return regular_expression


def remove_duplicated(list_words):
    """ Function will remove duplicate words on a list """
    seen = set()
    clean_list = []
    for word in list_words:
        if word not in seen:
            seen.add(word)
            clean_list.append(word)

    return clean_list


def word_counter(text: str, clean_words, list_words):
    """ Will check how many times a word is being repeated and set a counter for that word """
    seen = set()

    # Create a dictionary from the list and set all values to 0 (initiate counter)
    dictionary_word = {i: 1 for i in clean_words}

    for word in list_words:
        if word in seen:
            dictionary_word[word] += 1
        else:
            seen.add(word)

    return dictionary_word


with open(sys.argv[1], 'r') as myfile:
  story = myfile.read()


x = list_of_word(story.lower())
c = remove_duplicated(x)
d = word_counter(story, c, x)
od = collections.OrderedDict(sorted(d.items()))

file1 = open(sys.argv[2], "w")
for key in od:
    file1.write(str(key)+" "+str(od[key])+"\n")

file1.close()




