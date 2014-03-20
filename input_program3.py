#!/usr/bin/python
########Author Akshay Minocha ( ksnmi | minocha )##############
########mailto:akshayminocha5@gmail.com########################
import pickle
import string
import sys

def disambiguated_output(line):
  x=line[1:-1]   # ^ and $ symbols are ommitted   not liine.. this is per token
  tokens=[]
  word=""
  flag=0
  temp=0
  for i in range(0,len(x)-1): 
    if i<temp:
      continue
    if x[i]=="\\":
      word+=x[i]+x[i+1]
      temp=i+2
      print i, "change"
      continue
    if x[i]=="/":
      tokens+=[word] 
      word=""
      continue
    word+=x[i]
  word+=x[i+1]
  tokens+=[word]
  return tokens

def main():
  f=sys.stdin.readlines()
  english_wordlist=pickle.load(open("wordlist_dic"))
  d=[]
  for i in f:
    d+=[i.split()[0]]
  for line in d:
    text=disambiguated_output(line)  #line[1:-2].split("/")
    original_word=text[0]
    if original_word.lower() in english_wordlist:
      print original_word
      continue
    else:
      flag=0
      for i in text[1:]:
        if i.lower() in english_wordlist:
          print i
          flag=1
          break
      if flag==0:
        print original_word



if __name__=="__main__":
  main()
