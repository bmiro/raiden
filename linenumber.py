# -*- coding: utf-8 -*-

from sys import argv

if __name__ == '__main__':
   f = open(argv[1], 'r+')
   out = open(argv[2], 'a')
   i = 10000
   for line in f:
      line = str(i) + " " + line
      print line
      i += 10
      out.write(line)
   f.close()
   out.close()
