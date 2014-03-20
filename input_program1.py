#!/usr/bin/python
import sys
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

lines=sys.stdin.readlines()
for word in lines:
  words=word.split()
  c1=""
  temp=0
  dl=[]
  for j in words:
    c1=""
    for i in range(0,len(j)):
      if i<temp:
        continue
      if i=="\\":
        c1+=j[i]+j[i+1]
        temp=i+2
        continue
      c1+=j[i]
    dl+=[[c1,c1]]
  print " ".join(ambiguated_output(dl))
