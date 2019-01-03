# -*- coding: utf-8 -*-

"""Main module."""
import re
import os
from words_dictionary import words_dict

BASE_DIR = os.path.dirname(__file__)
class BoggleSolver():
    def __init__(self, grid):
        self.grid = grid.split()
        self.nrows, self.ncols = len(self.grid), len(self.grid[0])
        alphabet = ''.join(set(''.join(self.grid)))
        bogglable = re.compile('[' + alphabet + ']{3,}$', re.I).match
        #self.words = set(word.rstrip('\n') for word in open(words_file) if bogglable(word))
        self.words = set(words_dict.keys())
        self.prefixes = set(word[:i] for word in self.words  for i in range(2, len(word)+1))



    def solve(self):

        for y, row in enumerate(self.grid):
            for x, letter in enumerate(row):
                for result in self.extending(letter, ((x, y),)):
                    yield result

    def extending(self, prefix, path):
        if prefix in self.words:
            yield (prefix, path)
        for (nx, ny) in self.neighbors(path[-1]):
            if (nx, ny) not in path:
                prefix1 = prefix + self.grid[ny][nx]
                if prefix1 in self.prefixes:
                    for result in self.extending(prefix1, path + ((nx, ny),)):
                        yield result

    def neighbors(self, (x, y)):
        for nx in range(max(0, x-1), min(x+2, self.ncols)):
            for ny in range(max(0, y-1), min(y+2, self.nrows)):
                yield (nx, ny)

if __name__=="__main__":
    import sys
    grid = sys.argv[1]
    bs = BoggleSolver(grid)
    for w in bs.solve(): print w
#for x in solve(): print x
#print list(solve(), key=lambda (word, path): len(word))
