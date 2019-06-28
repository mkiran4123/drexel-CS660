#!/usr/bin/python3
import string


def getFrequencyDict(file_name):
    """ Returns a dictionary of each letter and its frequency """
    freq = {}
    count = 0
    for c in string.ascii_lowercase:
        freq[c] = 0

    for line in open(file_name, encoding="utf8"):
        for c in line.lower():
            if not c.isalpha():
                continue
            if c not in freq:
                continue
            freq[c] = freq[c] + 1
            count += 1
    for key in freq:
        freq[key] /= count
    return freq

def getFrequencyWordDict(file_name):
    freq = {}

    for line in open(file_name, encoding="utf8"):
        for word in line.lower().split():
            if not word:
                continue
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

    return freq

def RMSE(list1, list2):
    """ calculate root mean square error by summing the
    squares of each difference and returning the square root """
    sum = 0
    for i in range(len(list1)):
        sum += (list1[i] - list2[i]) ** 2
    return sum ** .5
