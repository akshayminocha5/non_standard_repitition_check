#!/usr/bin/python
import sys

lines=sys.stdin.readlines()
for word in lines:
  word=word.split()[0]
  c1=""
  temp=0
  for i in range(0,len(word)):
    if i<temp:
      continue
    if i=="\\":
      c1+=word[i]+word[i+1]
      temp=i+2
      continue
    c1+=word[i]
  
  print "^"+c1+"/"+c1+"$"
