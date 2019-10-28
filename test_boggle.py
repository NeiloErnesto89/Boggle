import unittest 
import boggle
from string import ascii_uppercase 

class test_boggle(unittest.TestCase):
    
    """
    our test suite for boggler solver 
    """ 
    
    #def test_is(self):
     #   self.assertEqual(1 ,1) #trivial example to ask if 1 = 0
        
    def test_can_create_empty_grid(self):
        """
        test to see if we can create an empty grid
        """
        
        grid = boggle.make_grid(0,0) # made make_grid method/function in boggle.py file
        self.assertEqual(len(grid), 0)
        
    def test_grid_coordinates(self):
        """
        a test to see if all the coordinates 
        inside of the grid can be accessed
        """
        grid =   boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid) # not in the grid 
        
    def test_grid_is_filled_with_letters(self):
        """
        test to ensure to that each coordinates on the grid
        contains letters 
        """
        grid = boggle.make_grid(2 ,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
