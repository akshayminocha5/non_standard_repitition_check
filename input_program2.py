#!/usr/bin/python
########Author Akshay Minocha ( ksnmi | minocha )##############
########mailto:akshayminocha5@gmail.com########################
import pickle
import string
import sys


def main():
  f=sys.stdin.readlines()
  english_wordlist=pickle.load(open("wordlist_dic"))
  d=[]
  for i in f:
    d+=[i.split()[0]]
  for line in d:
    text=line[1:-2].split("/")
    original_word=text[0]
    if original_word.lower() in english_wordlist:
      x="^"+original_word+"/"+original_word+"$"
      print x
      continue
    else:
      x="^"+original_word+"/"
      flag=0
      for i in text[1:]:
        if i.lower() in english_wordlist:
          x+=i+"$"
          flag=1
          break
      if flag==0:
        x+=original_word+"$"
      print x



if __name__=="__main__":
  main()
