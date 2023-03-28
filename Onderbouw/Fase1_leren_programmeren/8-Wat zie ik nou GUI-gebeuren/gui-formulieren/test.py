from random import choice, randint
from string import ascii_lowercase

print(' '.join(
    ['a'
    if randint(0, 1) == 0 
    else choice(ascii_lowercase)  
    for i in range(32)]))