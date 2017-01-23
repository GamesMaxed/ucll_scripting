from testing import *
from testing.tests import *
from testing.assertions import *


with cumulative, testedFunctionName("longestIncreasingSubsequence"):
    reftest()([])
    reftest()([0])
    reftest()([0,1,2,3,4,5])
    reftest()([5,1,2,3,0])
    reftest()([1,2,3,2,3,4])
    reftest()([1,5,2,6,3,7,4,8,5,9])
    reftest()([1,3,5,7,9,2,4,6,8])
    reftest()([1,3,5,7,9,2,4,6,8,10,12])
    reftest()([50,55,58,40,41,42,43,45,48,49,10,15,18])

