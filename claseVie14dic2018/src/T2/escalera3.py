#!/usr/bin/python

fil = 5
while fil >= 1:
   if fil % 2 != 0:
      col = 1
      while col <= fil:
         print col,
         col = col + 1
      print
      col = 1
      while col <= fil:
         print col,
         col = col + 1
      print
   fil = fil - 1

