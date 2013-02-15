# vim:encoding=utf-8:ts=2:sw=2:expandtab

import xp2xm
import sys

if len(sys.argv) == 1:
  infile = 'sample-input.txt'
elif len(sys.argv) == 2:
  infile = sys.argv[1]
else:
  print("Usage: python3.3 xp2xm-test.py [inputfile.txt]")
  sys.exit()


print('='*80)
data = open(infile, 'r')
print(data.read())
print()

print('='*80)
data = open(infile, 'r')
result = xp2xm.convert(data, Output='xml')
print(result)
print()

print('='*80)
data = open(infile, 'r')
result = xp2xm.convert(data, Output='prettyxml')
print(result)
print()

print('='*80)
data = open(infile, 'r')
result = xp2xm.convert(data, Output='dict')
print(result)
print()


