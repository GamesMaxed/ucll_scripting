from testing import *
from testing.tests import *
from testing.assertions import *


with all_or_nothing(), tested_function_name("find_episode_titles"):
    check = reftest()

    check('Breaking Bad')
    check('Westworld')
    check('Game of Thrones')
    check('The Wire')

    
with all_or_nothing(), tested_function_name("best_movie_from_year"):
    check = reftest()

    check(1968, 10000)
    check(2000, 10000)
    check(2016, 10000)

    
with all_or_nothing(), tested_function_name("series_average_ratings"):
    reftest()()




    
    
    
