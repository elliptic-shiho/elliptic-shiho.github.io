from ecpy import *
from math import *

def F(x):
  return x * x * x + 4 * x + 5;

def corresponding_y(x):
  return sqrt(F(x))

data = []

i = -1
while i < -0.95:
  data += [(i, corresponding_y(i)), (i, -corresponding_y(i))]
  i += 0.001

while i < 5:
  data += [(i, corresponding_y(i)), (i, -corresponding_y(i))]
  i += 0.01

res = '{\n'
for x,y in data:
  res += '\t%s:%s, \n' % (x, y)
res += '}\n'

open("data.json", "w").write(res)
