from string import ascii_uppercase
from random import choice 

def make_grid(width, height):
    """
    make empty boggle grid 
    """ 
    return {(row, col): choice(ascii_uppercase)
        for row in range (height) # remove ' ' and add choice()
        for col in range(width)}