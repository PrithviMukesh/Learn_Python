#This is an example of Word Frequency

import requests
from bs4 import BeautifulSoup
import operator

def word_freq(url):
    word_list = []
    soure_code = requests.get(url).text
    soup = BeautifulSoup(soure_code)
    for post_text in soup.findAll('a', {'class' : 'my-class'}):
        content = post_text.string
        words = content.lower().split()
        for single in words: #20
            print(single)
            word_list.append(single)
    clean_up(word_list)

def clean_up(word_list):
    clean_words = []
    for word in word_list:
        symbols = "!@#$%^&*()_+-{}|\:<>?';,./"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            clean_words.append(word)
    create_word_dictionary(clean_words)

def create_word_dictionary(clean_words):
    word_dic = {}
    for word in clean_words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    for key,value in sorted(word_dic.items() ,key = operator.itemgetter(1)):
        print(key,value)


word_freq('https://support.office.com/en-us/article/Delete-a-page-in-Word-174fedd3-b4e5-42e4-a4d0-5e25127a1404')


