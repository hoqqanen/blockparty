import numpy as np
from BlockParty import Board, standardBlocks


##Compute the average number of parties for the standard 8 block set
sample = 5000
b = Board(standardBlocks)
q = np.zeros(sample)

for i in xrange(sample):
  b.roll()
  q[i] = b.find_parties()

print q
print q.mean()
print np.histogram(q,bins=10)
print np.amax(q)
print np.amin(q)