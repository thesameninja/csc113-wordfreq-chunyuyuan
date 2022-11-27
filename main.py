import string
import time
import os
import random


#Useful links for you guys: 
#https://www.geeksforgeeks.org/with-statement-in-python/
#https://www.w3schools.com/python/python_dictionaries.asp
#https://www.w3schools.com/python/python_tuples.asp

#-Sohail Ahmad


#Code for reading the book.txt into python
filepath = "/home/np/GitHub/csc113-wordfreq-chunyuyuan/book.txt" #These file paths are specific to my local instance, either set it to your filepaths or find a way to have a relative path to the project.
out_filepath = "/home/np/GitHub/csc113-wordfreq-chunyuyuan/output.txt"
word_count = {}


#function to remove the punctuations 
def remove_punctuations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
    return line


#sorting the dictionary with tuple, then reversing the tuplef to get top to bottom.
def ordered_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key],key))
    sorted_values = sorted(sorted_values)

    sorted_values = sorted_values[::-1]
    return sorted_values


#using filepath to acces file, removing punctuations, 
with open(filepath, 'r') as fi:
    for line in fi:
        line = remove_punctuations(line)
        words = line.split()

        for words in words:
            words = words.lower()
            if words not in word_count:
                word_count[words] = 0
            word_count[words] += 1

#Output list of top words into output.txt
#https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
#refer to the stackoverflow for better understanding of the with block.

top_words = ordered_dict_by_freq(word_count)
for tuple_freq in top_words:
    count, word = tuple_freq
    with open("output.txt", "a") as f:
        print("{0:20}{1:8d}".format(word, count),file=f)


#Other team members can work here - Sohail>>> 
#You guys can start adding your code, we need to figure out multi-threading/processing
#implement a way to then measure the time taken for the program to run for each specification.
#-Sohail Ahmad 11/27/2022
