#!/usr/bin/python
#This is the script which works for the text written in English or INTENDED to be written in English. This text may or may not be grammatically correct. Our aim is to normalise the repititions in the word.
########Author Akshay Minocha ( ksnmi | minocha )##############
########mailto:akshayminocha5@gmail.com########################
import sys
import itertools
import string
special_characters=['^','$','/']
def ambiguated_output(list_of_tokens):
  dl=[]
  for word_token in list_of_tokens:
    s='^'
    s+=word_token[0]+"/"
    l=[]
    for word in word_token[1:]:
      if word in l:
        continue
      else:
        l+=[word]
    j='/'.join(l)
    s=s+j+'$'
    dl+=[s]
  return dl

def disambiguated_output_word(line):
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
      continue
    if x[i]=="/":
      tokens+=[word] 
      word=""
      continue
    word+=x[i]
  word+=x[i+1]
  tokens+=[word]
  return tokens

def check_repitition(word):
  # returns 1 if the number of characters is >=3 
  # returns 0 if it thinks the word has non repititive characters (otherwise)
  punc=string.punctuation
  if word[0] in punc:
    return 0
  flag_count=0
  flag=''
  for i in range(0,len(word)):
    if i==0:
      flag=word[0]
      flag_count=1
      continue
    else:
      if word[i]==flag:
        flag_count+=1
        if flag_count>2:
          return 1
      else:
        flag=word[i]
        flag_count=1
  return 0

def generate_variations(word):
  flag_count=0
  flag=''
  temp=word[0]
  list_of_rep=[]
  for i in range(0,len(word)):
    if i==0:
      flag=word[0]
      flag_count=1
      continue
    else:
      if word[i]==flag:
        flag_count+=1
        if flag_count>3:
          continue
        if flag_count>2:
          list_of_rep+=[len(temp)-2]
          continue
        else:
          temp+=word[i]
      else:
        flag=word[i]
        flag_count=1
        temp+=word[i]
  return (temp,list_of_rep)

def generate_all_variations(tuple_info):
  #0th -> original candiate normalised( 1stage )
  # all repititions which are detected earlier ( have either 1 or 2 repititions as the final output of this script)
  length=len(tuple_info[1])  # all the index positions where the repititions > 3 were made
  all_words=[]
  list_of_index=tuple_info[1]
  word=tuple_info[0]
  for x in map(''.join, itertools.product('01', repeat=length)):
    temp=word[:list_of_index[0]+1]
    flag=list_of_index[0]+2
    for i in range(0,len(x)):
      if x[i]=="1":
        temp+=word[list_of_index[i]]
      if i+1<len(x):
        temp+=word[flag:list_of_index[i+1]+1]
        flag=list_of_index[i+1]+2
      else:
        temp+=word[flag:]
    all_words+=[temp]
  return all_words

def main():
  #wordlist=pickle.load(open("wordlist_dic"))
  input1=sys.stdin.readlines()
  dl=[]
  for line in input1:
    dl+=[line.split()]
  for line in dl:
    new_sent=[]
    for token in line:
      new_sent+=[disambiguated_output_word(token)] # ,"token"  #token
    ntt=[]
    for word in new_sent:
      i=word[-1]
      if check_repitition(i)==1:
        gv=generate_all_variations(generate_variations(i))
        l=word[:2]+gv
        ntt+=[l]
      else:
        ntt+=[word]
    print " ".join(ambiguated_output(ntt))
  
if __name__=="__main__":
  main()


