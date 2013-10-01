from random import choice
import itertools
import numpy as np

def test_blocks(blockset):
  """
  Test that there are exactly 6 of each value of each attribute on each block
  """
  for attribute in [0,1,2]:
    for i in blockset:
      q = [0,0,0,0]
      for j in blockset[i]:
        for k in blockset[i][j]:
          q[k[attribute]]+=1
      for x in q:
        if x!=6:
          print i
          print j
          print k
          return False
  return True

standardBlocks = {'block1':
                  {'face1': [[1,0,0],[2,2,2],[0,3,1],[2,0,0]],
                  'face2': [[0,2,2],[2,1,1],[3,1,1],[1,0,2]],
                  'face3': [[2,1,3],[1,3,1],[0,3,3],[3,2,2]],
                  'face4': [[3,2,0],[3,1,3],[0,0,0],[3,3,3]],
                  'face5': [[1,1,1],[2,2,0],[1,3,3],[0,0,2]],
                  'face6': [[0,2,0],[3,3,1],[2,0,2],[1,1,3]]},
                'block2':
                  {'face1': [[2,2,1],[1,1,0],[0,0,3],[0,1,3]],
                  'face2': [[0,0,1],[1,2,0],[3,0,2],[3,3,0]],
                  'face3': [[2,1,2],[1,2,2],[2,1,0],[2,3,1]],
                  'face4': [[3,2,1],[0,1,1],[1,0,1],[3,0,0]],
                  'face5': [[2,2,3],[3,3,2],[1,0,3],[0,3,2]],
                  'face6': [[2,3,3],[0,3,0],[1,1,2],[3,2,3]]},
                'block3':
                  {'face1': [[0,3,2],[0,0,3],[3,3,2],[3,3,0]],
                  'face2': [[1,3,2],[2,2,3],[3,2,3],[0,2,1]],
                  'face3': [[3,1,0],[1,1,2],[3,2,1],[1,0,1]],
                  'face4': [[1,0,3],[0,0,1],[1,3,0],[0,2,3]],
                  'face5': [[2,0,1],[2,1,0],[0,3,0],[2,1,2]],
                  'face6': [[1,1,0],[3,1,2],[2,0,3],[2,2,1]]},
                'block4':
                  {'face1': [[3,1,3],[3,3,0],[3,0,0],[1,3,1]],
                  'face2': [[2,3,1],[2,0,2],[1,1,2],[3,0,2]],
                  'face3': [[0,2,0],[3,1,1],[0,0,3],[1,3,3]],
                  'face4': [[1,2,2],[1,2,0],[2,2,1],[2,0,0]],
                  'face5': [[0,0,1],[1,1,0],[0,2,2],[2,2,3]],
                  'face6': [[0,1,3],[2,3,3],[0,1,1],[3,3,2]]},
                'block5':
                  {'face1': [[0,3,1],[2,1,3],[3,3,1],[3,0,3]],
                  'face2': [[0,3,3],[1,2,3],[3,2,2],[2,3,2]],
                  'face3': [[3,3,3],[1,1,1],[1,2,1],[2,2,0]],
                  'face4': [[1,0,0],[2,2,2],[0,1,2],[3,2,0]],
                  'face5': [[2,3,0],[2,1,1],[0,1,0],[1,0,2]],
                  'face6': [[0,0,2],[1,1,3],[0,0,0],[3,0,1]]},
                'block6':
                  {'face1': [[3,1,2],[2,3,0],[1,3,2],[2,3,2]],
                  'face2': [[0,2,1],[1,3,0],[2,2,0],[1,1,3]],
                  'face3': [[3,1,0],[1,1,1],[3,3,3],[0,0,0]],
                  'face4': [[0,1,2],[1,2,3],[1,2,1],[2,0,3]],
                  'face5': [[3,0,1],[0,2,3],[0,1,0],[3,0,3]],
                  'face6': [[2,0,1],[3,3,1],[2,2,2],[0,0,2]]},
                'block7':
                  {'face1': [[3,1,1],[2,1,3],[1,2,2],[0,2,2]],
                  'face2': [[2,3,3],[2,3,1],[3,0,2],[1,2,0]],
                  'face3': [[3,2,2],[1,3,3],[3,2,0],[3,0,0]],
                  'face4': [[0,3,1],[3,1,3],[1,0,0],[2,0,0]],
                  'face5': [[0,1,3],[0,1,1],[2,0,2],[2,1,1]],
                  'face6': [[0,3,3],[1,0,2],[0,2,0],[1,3,1]]},
                'block8':
                  {'face1': [[3,0,1],[2,0,3],[0,3,2],[2,1,2]],
                  'face2': [[1,2,3],[2,0,1],[3,1,0],[2,1,0]],
                  'face3': [[1,0,1],[1,0,3],[1,3,0],[2,3,0]],
                  'face4': [[1,2,1],[0,1,2],[3,0,3],[0,2,3]],
                  'face5': [[0,3,0],[2,3,2],[3,2,3],[3,1,2]],
                  'face6': [[0,1,0],[0,2,1],[3,2,1],[1,3,2]]},
                  }

def is_party(symbols):
  party = True
  for attribute in [0,1,2]:
    if symbols[0][attribute] == symbols[1][attribute]:
      party = party and symbols[0][attribute] == symbols[2][attribute] and symbols[0][attribute] == symbols[3][attribute]
    else:
      party = party and symbols[0][attribute] != symbols[2][attribute] and symbols[0][attribute] != symbols[3][attribute]
      party = party and symbols[1][attribute] != symbols[2][attribute] and symbols[1][attribute] != symbols[3][attribute]
      party = party and symbols[2][attribute] != symbols[3][attribute]
  return party

class Block:
  def __init__(self, faces):
    self.faces = faces
    self.currentFaceIndex = 'face1'
  def roll(self):
    newFace = choice(self.faces.keys())
    self.currentFaceIndex = newFace
    self.currentFace = self.faces[newFace]
    return self.currentFace

class Board:
  def __init__(self, blockSet):
    self.blocks = []
    for block in blockSet:
      self.blocks.append(Block(blockSet[block]))
  def roll(self):
    for block in self.blocks:
      block.roll()
    return True
  def find_parties(self):
    parties = []
    for blockIndices in itertools.combinations(range(len(self.blocks)), 4):
      for symbolIndices in itertools.product(range(4),repeat=4):
        symbols = [self.blocks[blockIndices[0]].currentFace[symbolIndices[0]], 
                    self.blocks[blockIndices[1]].currentFace[symbolIndices[1]],
                    self.blocks[blockIndices[2]].currentFace[symbolIndices[2]],
                    self.blocks[blockIndices[3]].currentFace[symbolIndices[3]]]
        if is_party(symbols):
          parties.append(symbols)
    return len(parties)