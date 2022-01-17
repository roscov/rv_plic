
from enum import Enum
from math import ceil, log

def clog2(x):
  return ceil(log(x, 2))

class Access(Enum):
  RO = 1
  RW = 2
  WO = 3
  RESERVED = 4