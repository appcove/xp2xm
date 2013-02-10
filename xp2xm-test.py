# vim:encoding=utf-8:ts=2:sw=2:expandtab

import xp2xm

print('='*80)
data = open('sample-input.txt', 'r')
print(data.read())
print()

print('='*80)
data = open('sample-input.txt', 'r')
result = xp2xm.convert(data, Output='xml')
print(result)
print()

print('='*80)
data = open('sample-input.txt', 'r')
result = xp2xm.convert(data, Output='prettyxml')
print(result)
print()

print('='*80)
data = open('sample-input.txt', 'r')
result = xp2xm.convert(data, Output='dict')
print(result)
print()
