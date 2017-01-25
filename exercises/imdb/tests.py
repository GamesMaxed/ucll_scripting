from testing import *
from testing.tests import *
from testing.assertions import *


with allOrNothing(), testedFunctionName("findEpisodeTitles"):
    check = reftest()

    check('Breaking Bad')
    check('Westworld')
    check('Game of Thrones')
    check('The Wire')

    
with allOrNothing(), testedFunctionName("bestMovieFromYear"):
    check = reftest()

    check(1968)
    check(2000)
    check(2016)

    
with allOrNothing(), testedFunctionName("episodeCount"):
    reftest()()
    
    
with allOrNothing(), testedFunctionName("seriesAverageRatings"):
    reftest()()




    
    
    
