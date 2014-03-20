#!/usr/bin/python
import sys

lines=sys.stdin.readlines()
for word in lines:
  word=word.split()[0]
  print "^"+word+"/"+word+"$"
