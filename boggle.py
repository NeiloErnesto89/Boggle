from string import ascii_uppercase
from random import choice 

def make_grid(width, height):
    """
    make empty boggle grid 
    """ 
    return {(row, col): choice(ascii_uppercase)
        for row in range (height) # remove ' ' and add choice()
        for col in range(width)}
        
def neighbours_of_position(coords):
    """
    gets neighbours of given position
    """
    row = coords[0]
    col = coords[1]
    
    #assign each of neighbours corrds
    #top left to top rigt
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    # left to right (center)
    left = (row, col - 1)
    # the (row, col) cordinates  passed into this function are situated here
    right = (row, col + 1)
    
    #bottom-left to bottom-right
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return [top_left, top_center, top_right,
            left , right ,
            bottom_left, bottom_center, bottom_right]
    

def all_grid_neighbours(grid):
    """
    Get all neighbours possible for each position of grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours 
    
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string
    """
    return ''.join([grid[p] for p in path])

"""    
def word_in_dictionary(word, dict): # func removed due to partial words adaptation
    return word in dict             # served it's purpose, we now can access set of words directly
"""

def search(grid, dictionary):
    """
    Search through the paths to locate words by matching
    strings to words in a dictionary
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
    
    def do_search(path): # nested function
        word = path_to_word(grid, path)
        if word in full_words: # word_in_dictionary(word, dictionary): # word in dictionary: - modified again
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
def get_dictionary(dictionary_file):
    """
    Load dictionary file
    """
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
    
    return full_words, stems 

        #{w.strip().upper() for w in f} # removed a tab for most recent
        #[w.strip().upper() for w in f] #formerly a list, now a set with {} 

def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))
    
       
    """
    words = search(grid, dictionary)
    for word in words:
        print(word)
    print("Found %s word(s)" % len(words)) # previously underneath dictionary in main() funct
    """
    
        
def main():
    """
    This is the function that will run the whole project!!
    """
    grid = make_grid(3, 3) # change to 3x3
    dictionary = get_dictionary("words.txt")
    words = search(grid, dictionary)
    display_words(words)

if __name__ == "__main__":
    # Code in here will only execution when the file is run directly    
    main()