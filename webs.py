import re
import string
from collections import Counter
n=5

def get_statistics(data):
    """To get lines,words,unique words from there function
    :parameter=data form function
    :return=statistics """

    lines = get_lines(data)
    words= get_words(lines)
    unique_words=set(words)
    top_n_words=get_top_n_words(words,n)
    statistics ={'line count':len(lines),'words count':len(words),'unique words':len(unique_words),
                 'top_words':top_n_words}
    return statistics

def get_lines(data):
    """To find no. of in the sentence
    :parameter=data, from data find to no. of lines
    :return line to main function"""
    lines=[]
    for para in data:
        para_lines = re.split('[.!?]+',para)
        lines.extend(para_lines)
    return lines


def clean_string(lines):
    """To remove punctuation from sentence
    :parameter=line to remove punctuation and to be returned
     :return=cleaned_lines"""
    st = str.maketrans("", "", string.punctuation)
    cleaned_lines = [line.translate(st).lower().strip() for line in lines if line]
    return cleaned_lines

def get_words(lines):
    """To find no. of words from lines
    :parameter=lines to count the word in the line to be returned
    :return the words from the line"""

    words =[]
    for line in lines:
        words.extend(line.split())
    return words

def get_top_n_words(words,n):
    """Get the top n words from the given list of the words
    :parameter words,n count no.of most words
    :return the n words"""

    stopwords=get_stopwords()
    cleaned_lines = [word for word in words if word not in stopwords]
    return Counter(cleaned_lines).most_common(n)


def get_stopwords():
    """ read the file stopwords get the words from stopwords
    :return= the stopwords"""
    with open('stopwords.txt', "r") as fp:
        words=fp.readlines()
        stopwords   =[word.rstrip('\n') for word in words]
        return stopwords
